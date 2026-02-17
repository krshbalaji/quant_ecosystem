from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("dashboard.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/leaderboard")
def leaderboard():
    return render_template("leaderboard.html")


@app.route("/sparks")
def sparks():
    return render_template("sparks.html")
