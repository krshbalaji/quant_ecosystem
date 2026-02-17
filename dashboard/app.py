from flask import Flask, render_template, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__, template_folder="templates")


# SAFE STATE READER
def read_meta_state():

    path = "data/meta_state.json"

    if not os.path.exists(path):

        return {
            "mode": "PAPER",
            "equity": 0,
            "regime": "UNKNOWN",
            "allocation_mode": "IDLE",
            "recovery": False,
            "last_update": "Never",
            "last_strategy": "None"
        }

    try:

        with open(path, "r") as f:
            return json.load(f)

    except:

        return {
            "mode": "ERROR",
            "equity": 0,
            "regime": "ERROR",
            "allocation_mode": "ERROR",
            "recovery": False,
            "last_update": "ERROR",
            "last_strategy": "ERROR"
        }


@app.route("/")
def home():

    return render_template("dashboard.html")


@app.route("/dashboard")
def dashboard():

    state = read_meta_state()

    return render_template(
        "dashboard.html",
        state=state
    )


@app.route("/leaderboard")
def leaderboard():

    strategies = []

    if os.path.exists("strategies"):

        strategies = sorted(os.listdir("strategies"))

    return render_template(
        "leaderboard.html",
        strategies=strategies
    )


@app.route("/sparks")
def sparks():

    sparks = []

    if os.path.exists("strategies"):

        for s in sorted(os.listdir("strategies")):

            sparks.append(f"Spark Generated: {s}")

    return render_template(
        "sparks.html",
        sparks=sparks
    )


@app.route("/api/state")
def api_state():

    return jsonify(read_meta_state())


@app.route("/health")
def health():

    return {"status": "running", "time": str(datetime.now())}


# REQUIRED BY main.py
def run_dashboard():

    print("Dashboard running at http://127.0.0.1:5000")

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
        use_reloader=False
    )


# standalone mode
if __name__ == "__main__":

    run_dashboard()
