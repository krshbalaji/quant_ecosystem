# dashboard/app.py

from flask import Flask, render_template, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__, template_folder="templates")

DATA_DIR = "data"


# Safe JSON loader
def safe_load(filename, default):

    try:
        path = os.path.join(DATA_DIR, filename)

        if os.path.exists(path):
            with open(path, "r") as f:
                return json.load(f)

    except Exception as e:
        print("JSON load error:", e)

    return default


# Dashboard page
@app.route("/")
@app.route("/dashboard")
def dashboard():

    return render_template("dashboard.html")


# Leaderboard page
@app.route("/leaderboard")
def leaderboard():

    return render_template("leaderboard.html")


# Sparks page
@app.route("/sparks")
def sparks():

    return render_template("sparks.html")


# REALTIME STATUS API
@app.route("/api/status")
def api_status():

    meta = safe_load("meta_state.json", {})
    performance = safe_load("performance.json", {})
    elite = safe_load("elite.json", [])

    return jsonify({

        "time": datetime.now().strftime("%H:%M:%S"),

        "mode": meta.get("mode", "PAPER"),

        "equity": performance.get("equity", 8000),

        "pnl": performance.get("pnl", 0),

        "trades": performance.get("trades", 0),

        "winrate": performance.get("winrate", 0),

        "active_strategy":
            meta.get("active_strategy", "None"),

        "elite_count": len(elite)

    })


# Leaderboard API
@app.route("/api/leaderboard")
def api_leaderboard():

    elite = safe_load("elite.json", [])

    return jsonify(elite)


# Sparks API
@app.route("/api/performance")
def api_performance():

    perf = safe_load("performance.json", {})

    return jsonify(perf)


def run_dashboard():

    print("🏛 Realtime Institutional Dashboard running")

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
        threaded=True
    )
