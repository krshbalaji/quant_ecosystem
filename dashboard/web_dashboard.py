from flask import Flask, jsonify, render_template_string
import threading
import time
import math
import random

app = Flask(__name__)

# =========================
# LIVE DATA STORE (shared)
# =========================
STATE = {
    "capital": 0,
    "pnl": 0,
    "trades": 0,
    "equity": [],
    "returns": [],
    "positions": [],
    "strategies": []
}


# =================================
# Called from Engine to update data
# =================================
def update_data(pnl, trades, capital, positions=None, strategies=None):
    STATE["pnl"] = pnl
    STATE["trades"] = trades
    STATE["capital"] = capital

    STATE["equity"].append(capital + pnl)

    if len(STATE["equity"]) > 1:
        r = STATE["equity"][-1] - STATE["equity"][-2]
        STATE["returns"].append(r)

    if positions:
        STATE["positions"] = positions

    if strategies:
        STATE["strategies"] = strategies

    if strategies:
        STATE["strategies"] = strategies

    STATE["selected_strategy"] = engine.current_strategy
    STATE["mode"] = engine.mode
    STATE["confidence"] = engine.ml_confidence
    STATE["drawdown"] = portfolio.get_drawdown()
    STATE["equity"] = portfolio.get_equity_curve()
    STATE["health"] = core.health.evaluate()

# =========================
# Sharpe ratio
# =========================
def sharpe():
    r = STATE["returns"]
    if len(r) < 5:
        return 0
    mean = sum(r)/len(r)
    std = (sum((x-mean)**2 for x in r)/len(r))**0.5
    if std == 0:
        return 0
    return round((mean/std)*math.sqrt(252), 2)


# =========================
# API endpoint
# =========================
@app.route("/data")
def data():
    return jsonify({
        **STATE,
        "sharpe": sharpe()
    })

@app.route("/walkforward")
def walkforward():
    try:
        df = pd.read_csv("reports/walkforward_results.csv")
        return df.to_json(orient="records")
    except:
        return jsonify([])

@app.route("/drawdown")
def drawdown():
    try:
        df = pd.read_csv("reports/equity_curve.csv")
        peak = df["equity"].cummax()
        dd = (peak - df["equity"]) / peak
        return dd.to_json(orient="values")
    except:
        return jsonify([])

@app.route("/risk_status")
def risk_status():
    try:
        df = pd.read_csv("reports/equity_curve.csv")
        peak = df["equity"].max()
        current = df["equity"].iloc[-1]
        dd = (peak - current) / peak

        if dd < 0.05:
            status = "GREEN"
        elif dd < 0.15:
            status = "YELLOW"
        else:
            status = "RED"

        return jsonify({"status": status})
    except:
        return jsonify({"status": "UNKNOWN"})

@app.route("/sparks")
def sparks():
    import json
    with open("brain/spark_vault.json", "r") as f:
        data = json.load(f)
    return jsonify(data)

@app.route("/leaderboard")
def contributor_board():
    from spark.leaderboard import leaderboard
    return leaderboard()

@app.route("/ml_confidence")
def ml_confidence():
    return jsonify({"confidence": engine.get_ml_confidence()})

# =========================
# UI
# =========================
HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Quant Ecosystem</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<style>
body{
    background:#0e0e0e;
    color:white;
    font-family:Arial;
    padding:15px;
}
.card{
    background:#1c1c1c;
    padding:12px;
    border-radius:10px;
    display:inline-block;
    margin:6px;
    min-width:120px;
    text-align:center;
}
table{
    width:100%;
    border-collapse:collapse;
}
th,td{
    padding:8px;
    border-bottom:1px solid #333;
}
canvas{max-height:250px;}
@media(max-width:700px){
    .card{width:45%;}
}
</style>
</head>

<body>

<h2>🚀 Quant Ecosystem Pro Dashboard</h2>

<div>
<div class="card">Capital ₹ <b id="cap">0</b></div>
<div class="card">PnL <b id="pnl">0</b></div>
<div class="card">Trades <b id="trades">0</b></div>
<div class="card">Sharpe <b id="sharpe">0</b></div>
<div class="card">AI Strategy: {{ selected_strategy }}</div>
<div class="card">
🧠 Mode: {{mode}} <br>
Strategy: {{selected_strategy}}
</div>
<div class="card">
🧠 Confidence: {{confidence}} %
</div>
</div>

<h2>📈 Options Dashboard</h2>

<table>
<tr>
<th>Symbol</th>
<th>Type</th>
<th>Qty</th>
<th>PnL</th>
</tr>

{% for o in options %}
<tr>
<td>{{o.symbol}}</td>
<td>{{o.type}}</td>
<td>{{o.qty}}</td>
<td>{{o.pnl}}</td>
</tr>
{% endfor %}
</table>

<h3>📈 Equity Curve</h3>
<canvas id="eq"></canvas>

<h3>🔥 Trade Heatmap</h3>
<canvas id="heat"></canvas>

<h3>Live Drawdown</h3>
<div id="drawdown"></div>

<h3>Risk Heat</h3>
<div id="riskMeter"></div>

<h3>📌 Positions</h3>
<table>
<thead><tr><th>Symbol</th><th>Side</th><th>Qty</th><th>PnL</th></tr></thead>
<tbody id="pos"></tbody>
</table>

<h3>🏆 Strategy Ranking</h3>
<table>
<thead><tr><th>Name</th><th>PnL</th><th>Trades</th></tr></thead>
<tbody id="strat"></tbody>
</table>

<h3>Walk Forward Performance</h3>
<canvas id="wfChart"></canvas>

<h3>Live Drawdown</h3>
<canvas id="ddChart"></canvas>

<h3>Risk Heat</h3>
<div id="riskBox"></div>

<script>
let eqChart = new Chart(document.getElementById('eq'),{
type:'line',
data:{labels:[],datasets:[{label:'Equity',data:[]}]}
});

let heatChart = new Chart(document.getElementById('heat'),{
type:'bar',
data:{labels:[],datasets:[{label:'Returns',data:[]}]}
});

async function refresh(){
let r = await fetch('/data');
let d = await r.json();

cap.innerText=d.capital;
pnl.innerText=d.pnl;
trades.innerText=d.trades;
sharpe.innerText=d.sharpe;

eqChart.data.labels=d.equity.map((_,i)=>i);
eqChart.data.datasets[0].data=d.equity;
eqChart.update();

heatChart.data.labels=d.returns.map((_,i)=>i);
heatChart.data.datasets[0].data=d.returns;
heatChart.update();

document.getElementById("drawdown").innerText = 
    "Drawdown: " + (data.drawdown * 100).toFixed(2) + "%";

if (data.health === "HEALTHY") {
    riskMeter.innerHTML = "🟢 HEALTHY";
}
else if (data.health === "CAUTION") {
    riskMeter.innerHTML = "🟡 CAUTION";
}
else {
    riskMeter.innerHTML = "🔴 CRITICAL";
}

fetch('/walkforward')
.then(res => res.json())
.then(data => {
    const labels = data.map((_,i) => i+1);
    const values = data.map(d => d.return);

    new Chart(document.getElementById('wfChart'), {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Walk Forward Return',
                data: values,
                borderColor: 'blue'
            }]
        }
    });
});

fetch('/drawdown')
.then(res => res.json())
.then(data => {
    new Chart(document.getElementById('ddChart'), {
        type: 'line',
        data: {
            labels: data.map((_,i)=>i+1),
            datasets: [{
                label: 'Drawdown',
                data: data,
                borderColor: 'red'
            }]
        }
    });
});

fetch('/risk_status')
.then(res => res.json())
.then(data => {
    const box = document.getElementById('riskBox');
    box.innerText = data.status;

    if(data.status=="GREEN") box.style.color="green";
    if(data.status=="YELLOW") box.style.color="orange";
    if(data.status=="RED") box.style.color="red";
});

pos.innerHTML="";
d.positions.forEach(p=>{
pos.innerHTML+=`<tr>
<td>${p.symbol}</td>
<td>${p.side}</td>
<td>${p.qty}</td>
<td>${p.pnl}</td>
</tr>`;
});

strat.innerHTML="";
d.strategies.sort((a,b)=>b.pnl-a.pnl).forEach(s=>{
strat.innerHTML+=`<tr>
<td>${s.name}</td>
<td>${s.pnl}</td>
<td>${s.trades}</td>
</tr>`;
});
}

setInterval(refresh,2000);
</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

import json
from spark.evaluator import eevaluate_spark



@app.route("/sparks")
def view_sparks():
    try:
        with open("brain/spark_vault.json", "r") as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/leaderboard")
def view_leaderboard():
    try:
        board = get_leaderboard()
        return jsonify(board)
    except Exception as e:
        return jsonify({"error": str(e)})
