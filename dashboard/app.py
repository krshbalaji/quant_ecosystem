from flask import Flask, render_template, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

DATA_DIR = "data"


def load_json(filename, default):
    try:
        path = os.path.join(DATA_DIR, filename)
        if os.path.exists(path):
            with open(path, "r") as f:
                return json.load(f)
    except:
        pass
    return default


@app.route("/")
@app.route("/dashboard")
def dashboard():

    meta = load_json("meta_state.json", {})
    performance = load_json("performance.json", {})
    elite = load_json("elite.json", [])

    return render_template(
        "dashboard.html",
        meta=meta,
        performance=performance,
        elite=elite,
        now=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )


@app.route("/leaderboard")
def leaderboard():

    elite = load_json("elite.json", [])

    elite_sorted = sorted(
        elite,
        key=lambda x: x.get("score", 0),
        reverse=True
    )

    return render_template(
        "leaderboard.html",
        strategies=elite_sorted
    )


@app.route("/sparks")
def sparks():

    performance = load_json("performance.json", {})

    return render_template(
        "sparks.html",
        performance=performance
    )


# LIVE DATA API FOR REALTIME UI

@app.route("/api/status")
def api_status():

    meta = load_json("meta_state.json", {})
    performance = load_json("performance.json", {})

    return jsonify({
        "meta": meta,
        "performance": performance,
        "time": datetime.now().isoformat()
    })


def run_dashboard():
    print("🏛 Institutional Dashboard running at http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000, debug=False)
