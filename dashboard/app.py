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
