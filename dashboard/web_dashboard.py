from flask import Flask, jsonify, render_template_string
import pandas as pd
import os

app = Flask(__name__)

HTML = """
<html>
<head>
<title>Quant Ecosystem Dashboard</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
body { background:#111; color:white; font-family:Arial; }
.card { margin:20px; padding:20px; background:#222; border-radius:10px; }
</style>
</head>

<body>

<h2>🚀 Quant Ecosystem Live Dashboard</h2>

<div class="card">
<h3>Live PnL: ₹ <span id="pnl">0</span></h3>
<h3>Total Trades: <span id="trades">0</span></h3>
<h3>Status: <span id="status">RUNNING</span></h3>
</div>

<div class="card">
<canvas id="chart"></canvas>
</div>

<script>

let ctx = document.getElementById('chart');

let chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Equity Curve',
            data: [],
            borderColor: 'lime',
            fill:false
        }]
    }
});

async function update() {
    let res = await fetch('/data');
    let d = await res.json();

    document.getElementById('pnl').innerText = d.pnl;
    document.getElementById('trades').innerText = d.trades;
    document.getElementById('status').innerText = d.status;

    chart.data.labels = d.labels;
    chart.data.datasets[0].data = d.equity;
    chart.update();
}

setInterval(update, 3000);
update();

</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


@app.route("/data")
def data():

    if os.path.exists("journal/trades.csv"):
        df = pd.read_csv("journal/trades.csv")
        equity = df["capital"].tolist()
        pnl = equity[-1] - equity[0] if len(equity) > 1 else 0
        trades = len(df)
        labels = list(range(len(equity)))
    else:
        equity = []
        pnl = 0
        trades = 0
        labels = []

    return jsonify({
        "pnl": round(pnl,2),
        "trades": trades,
        "status": "RUNNING",
        "equity": equity,
        "labels": labels
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
