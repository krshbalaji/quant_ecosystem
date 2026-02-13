from flask import Flask, jsonify, render_template_string
import threading
import webbrowser
import time
import random

app = Flask(__name__)

# ===============================
# GLOBAL LIVE DATA STORE
# ===============================
DATA = {
    "pnl": 0,
    "capital": 0,
    "trades": 0,
    "win_rate": 0,
    "positions": [],
    "orders": [],
    "equity": []
}


# ===============================
# ENGINE → DASHBOARD updater
# call this from runner
# ===============================
def update_data(pnl, trades, capital, positions=None, orders=None):
    DATA["pnl"] = pnl
    DATA["trades"] = trades
    DATA["capital"] = capital

    if positions:
        DATA["positions"] = positions

    if orders:
        DATA["orders"] = orders

    DATA["equity"].append(pnl)


# ===============================
# API
# ===============================
@app.route("/data")
def data():
    return jsonify(DATA)


# ===============================
# UI
# ===============================
HTML = """
<!doctype html>
<html>
<head>
<title>Quant Ecosystem Dashboard</title>
<meta http-equiv="refresh" content="3">
<style>
body{font-family:Arial;background:#111;color:white}
.card{background:#1e1e1e;padding:12px;margin:8px;border-radius:8px;display:inline-block}
table{width:100%;border-collapse:collapse}
td,th{padding:6px;border-bottom:1px solid #333;text-align:center}
.green{color:#00ff7f}
.red{color:#ff5252}
</style>
</head>

<body>

<h2>🚀 Quant Ecosystem Live Dashboard</h2>

<div>
<div class="card">💰 Capital: {{capital}}</div>
<div class="card">📈 PnL: <span class="{{ 'green' if pnl>=0 else 'red' }}">{{pnl}}</span></div>
<div class="card">🔁 Trades: {{trades}}</div>
</div>

<h3>📊 Equity Curve</h3>
<div>
{% for e in equity[-50:] %}
<span style="font-size:10px">{{e}}, </span>
{% endfor %}
</div>

<h3>📌 Positions</h3>
<table>
<tr><th>Symbol</th><th>Side</th><th>Qty</th><th>PnL</th></tr>
{% for p in positions %}
<tr>
<td>{{p.symbol}}</td>
<td>{{p.side}}</td>
<td>{{p.qty}}</td>
<td>{{p.pnl}}</td>
</tr>
{% endfor %}
</table>

<h3>📜 Orders</h3>
<table>
<tr><th>Symbol</th><th>Side</th><th>Price</th></tr>
{% for o in orders %}
<tr>
<td>{{o.symbol}}</td>
<td>{{o.side}}</td>
<td>{{o.price}}</td>
</tr>
{% endfor %}
</table>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML, **DATA)


# ===============================
# START SERVER
# ===============================
def start_dashboard():
    threading.Timer(1, lambda: webbrowser.open("http://localhost:5000")).start()
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    start_dashboard()
