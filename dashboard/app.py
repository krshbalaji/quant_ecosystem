from flask import Flask, jsonify
import json
import os

app = Flask(__name__)


@app.route("/")
def home():

    return jsonify({
        "status": "Quant Ecosystem Running",
        "engine": "ACTIVE"
    })


@app.route("/performance")
def performance():

    file = "data/strategy_performance.json"

    if os.path.exists(file):

        return jsonify(json.load(open(file)))

    return jsonify({})


@app.route("/health")
def health():

    return jsonify({
        "system": "healthy"
    })

@app.route("/dashboard")
def dashboard():
    return """
    <h1>Quant Ecosystem Dashboard</h1>
    <p>System Active</p>
    <p><a href='/spark'>Spark Leaderboard</a></p>
    """

@app.route("/spark")
def spark():
    return jsonify({
        "strategies": 32,
        "status": "Spark Engine Active"
    })

@app.route("/leaderboard")
def leaderboard():
    return jsonify({
        "top_strategy": "strategy_gen_42522",
        "confidence": 0.74
    })