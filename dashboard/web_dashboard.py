from flask import Flask, jsonify, render_template_string
import threading
import webbrowser
import numpy as np

app = Flask(__name__)

DATA = {
    "capital": 0,
    "pnl": 0,
    "trades": 0,
    "positions": [],
    "orders": [],
    "equity": [],
    "daily": [],
    "strategies": []
}


# =====================================================
# CALCULATIONS
# =====================================================
def sharpe_ratio(equity):
    if len(equity) < 5:
        return 0
    returns = np.diff(equity)
    if np.std(returns) == 0:
        return 0
    return round((np.mean(returns) / np.std(returns)) * np.sqrt(252), 2)


# =====================================================
# ENGINE CALL
# =====================================================
def update_data(pnl, trades, capital, positions=None, orders=None, strategy_stats=None):
    DATA["pnl"] = pnl
    DATA["trades"] = trades
    DATA["capital"] = capital

    if positions:
        DATA["positions"] = positions

    if orders:
        DATA["orders"] = orders

    if strategy_stats:
        DATA["strategies"] = strategy_stats

    DATA["equity"].append(pnl)
    DATA["daily"].append(pnl)


# =====================================================
# API
# =====================================================
@app.route("/data")
def data():
    return jsonify(DATA)


# =====================================================
# DASHBOARD UI
# =====================================================
HTML = """
<!doctype html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="3">

<style>
body{background:#111;color:white;font-family:Arial}
.card{background:#1e1e1e;padding:10px;margin:5px;border-radius:8px;display:inline-block}
table{width:100%;margin-top:10px}
td,th{padding:6px;border-bottom:1px solid #333;text-align:center}
.green{color:#00ff7f}
.red{color:#ff5252}
.heat{display:inline-block;width:14px;height:14px;margin:2px}
</style>
</head>

<body>

<h2>🚀 Quant Ecosystem</h2>

<div>
<div class="card">Capital ₹ {{capital}}</div>
<div class="card">PnL <span class="{{'green' if pnl>=0 else 'red'}}">{{pnl}}</span></div>
<div class="card">Trades {{trades}}</div>
<div class="card">Sharpe {{sharpe}}</div>
</div>

<h3>📊 Equity Curve</h3>
<div style="font-size:10px">
{% for e in equity[-50:] %} {{e}}, {% endfor %}
</div>

<h3>🔥 Trade Heatmap</h3>
{% for d in daily[-60:] %}
<div class="heat" style="background:{{'#00aa55' if d>=0 else '#aa0033'}}"></div>
{% endfor %}

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

<h3>⚙ Strategy Comparison</h3>
<table>
<tr><th>Name</th><th>PnL</th><th>Trades</th></tr>
{% for s in strategies %}
<tr>
<td>{{s.name}}</td>
<td>{{s.pnl}}</td>
<td>{{s.trades}}</td>
</tr>
{% endfor %}
</table>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(
        HTML,
        **DATA,
        sharpe=sharpe_ratio(DATA["equity"])
    )


def start_dashboard():
    threading.Timer(1, lambda: webbrowser.open("http://localhost:5000")).start()
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    start_dashboard()
