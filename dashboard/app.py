from flask import Flask, render_template, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

META_FILE = os.path.join(BASE_DIR, "data", "meta_state.json")
STRATEGY_DIR = os.path.join(BASE_DIR, "strategies")


def load_meta():
    if os.path.exists(META_FILE):
        try:
            with open(META_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}


def get_strategies():
    if not os.path.exists(STRATEGY_DIR):
        return []
    return [
        f for f in os.listdir(STRATEGY_DIR)
        if f.endswith(".py")
    ]


@app.route("/")
@app.route("/dashboard")
def dashboard():

    meta = load_meta()

    strategies = get_strategies()

    data = {
        "equity": meta.get("equity", 0),
        "mode": meta.get("mode", "UNKNOWN"),
        "regime": meta.get("regime", "UNKNOWN"),
        "allocation": meta.get("allocation_mode", "UNKNOWN"),
        "recovery": meta.get("recovery", False),
        "strategy_count": len(strategies),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return render_template("dashboard.html", data=data)


@app.route("/leaderboard")
def leaderboard():

    strategies = get_strategies()

    ranked = sorted(strategies)

    return render_template("leaderboard.html", strategies=ranked)


@app.route("/sparks")
def sparks():

    strategies = get_strategies()

    return render_template("sparks.html", strategies=strategies)


@app.route("/api/status")
def api_status():

    meta = load_meta()

    return jsonify(meta)


def run_dashboard():

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
