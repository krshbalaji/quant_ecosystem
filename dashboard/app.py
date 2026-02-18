from flask import Flask, jsonify, render_template
import threading
import time

from core.mode_controller import get_mode
from core.meta_intelligence import meta_intelligence
from core.performance_tracker import get_performance_snapshot

app = Flask(__name__)


# ---------------------------
# LIVE STATE ENDPOINT
# ---------------------------
@app.route("/api/state")
def api_state():
    try:
        from core.performance_tracker import performance_tracker
        from core.meta_intelligence import meta_intelligence

        snapshot = performance_tracker.get_snapshot()

        return jsonify({
            "mode": snapshot.get("mode", "PAPER"),
            "equity": snapshot.get("equity", 8000),
            "pnl": snapshot.get("pnl", 0),
            "trades": snapshot.get("trades", 0),
            "winrate": snapshot.get("winrate", 0),
            "regime": getattr(meta_intelligence, "current_regime", "UNKNOWN")
        })

    except Exception as e:
        print("API STATE ERROR:", e)
        return jsonify({
            "mode": "ERROR",
            "equity": 0,
            "pnl": 0,
            "trades": 0,
            "winrate": 0,
            "regime": "ERROR"
        })


# ---------------------------
# DASHBOARD PAGE
# ---------------------------
@app.route("/")
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ---------------------------
# RUN FUNCTION
# ---------------------------
def run_dashboard():
    app.run(host="0.0.0.0", port=5000, debug=True)

from core.telemetry import get_leaderboard

@app.route("/api/leaderboard")
def api_leaderboard():
    return jsonify(get_leaderboard())

@app.route("/api/ai")
def api_ai():
    return jsonify({
        "regime": meta_intelligence.current_regime,
        "suggestion": "Reduce exposure" if meta_intelligence.current_regime == "VOLATILE" else "Increase allocation"
    })
