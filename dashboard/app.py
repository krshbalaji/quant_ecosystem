# dashboard/app.py

from flask import Flask, render_template, jsonify
import datetime
import os
import json

from core.mode_controller import mode_controller
from core.meta_intelligence import meta_intelligence
from core.performance_tracker import performance_tracker

app = Flask(__name__)

DATA_FILE = "data/telemetry.json"


def load_telemetry():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}


@app.route("/")
@app.route("/dashboard")
def dashboard():

    telemetry = load_telemetry()

    data = {
        "time": datetime.datetime.now().strftime("%H:%M:%S"),
        "mode": mode_controller.get_mode(),
        "equity": performance_tracker.get_equity(),
        "pnl": performance_tracker.get_pnl(),
        "trades": performance_tracker.get_trade_count(),
        "winrate": performance_tracker.get_winrate(),
        "regime": meta_intelligence.predict_regime(),
        "last_strategy": telemetry.get("last_strategy", "None"),
        "equity_curve": telemetry.get("equity_curve", []),
        "strategy_scores": telemetry.get("strategy_scores", {})
    }

    return render_template("ai_dashboard.html", data=data)


@app.route("/api/live")
def live_data():
    return jsonify(load_telemetry())


def run_dashboard():
    print("🚀 Institutional Dashboard running at http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000, debug=False)
