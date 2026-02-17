import json
import os
import threading
import time
from datetime import datetime
from flask import Flask, render_template, jsonify

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
META_FILE = os.path.join(BASE_DIR, "data", "meta_state.json")
PERF_FILE = os.path.join(BASE_DIR, "data", "performance.json")
TRADE_FILE = os.path.join(BASE_DIR, "data", "trades.json")

app = Flask(__name__, template_folder="templates", static_folder="static")

# Global realtime state
dashboard_state = {
    "mode": "PAPER",
    "equity": 0,
    "pnl": 0,
    "trades": 0,
    "winrate": 0,
    "active_strategy": "None",
    "last_update": "",
    "strategies": {},
    "equity_curve": [],
    "pnl_curve": [],
}

# ----------------------------------------
# Load state safely
# ----------------------------------------

def load_json(path, default):
    try:
        if os.path.exists(path):
            with open(path, "r") as f:
                return json.load(f)
    except:
        pass
    return default


# ----------------------------------------
# Realtime update loop
# ----------------------------------------

def realtime_updater():
    while True:
        meta = load_json(META_FILE, {})
        perf = load_json(PERF_FILE, {})
        trades = load_json(TRADE_FILE, [])

        dashboard_state["mode"] = meta.get("mode", "PAPER")
        dashboard_state["equity"] = meta.get("equity", 0)
        dashboard_state["active_strategy"] = meta.get("strategy", "None")
        dashboard_state["last_update"] = datetime.now().strftime("%H:%M:%S")

        dashboard_state["strategies"] = perf.get("strategies", {})
        dashboard_state["equity_curve"] = perf.get("equity_curve", [])
        dashboard_state["pnl_curve"] = perf.get("pnl_curve", [])

        dashboard_state["trades"] = len(trades)

        wins = sum(1 for t in trades if t.get("pnl", 0) > 0)
        dashboard_state["winrate"] = (
            round(wins / len(trades) * 100, 2) if trades else 0
        )

        dashboard_state["pnl"] = sum(t.get("pnl", 0) for t in trades)

        time.sleep(1)


# Start realtime thread
threading.Thread(target=realtime_updater, daemon=True).start()

# ----------------------------------------
# Routes
# ----------------------------------------

@app.route("/")
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/api/state")
def api_state():
    return jsonify(dashboard_state)


@app.route("/leaderboard")
def leaderboard():
    return jsonify(dashboard_state["strategies"])


@app.route("/sparks")
def sparks():
    spark_file = os.path.join(BASE_DIR, "data", "spark_log.json")
    return jsonify(load_json(spark_file, []))


# ----------------------------------------

def run_dashboard():
    print("🚀 Institutional Dashboard running at http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)
