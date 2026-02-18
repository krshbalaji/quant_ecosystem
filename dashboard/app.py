from flask import Flask, render_template, jsonify
from core.live_state import live_state

app = Flask(__name__)

@app.route("/")
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/api/state")
def state():
    return jsonify(live_state)

def run_dashboard():
    print("🚀 Dashboard running at http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000)
