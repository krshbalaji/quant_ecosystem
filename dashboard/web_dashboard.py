from flask import Flask, jsonify
from engine.portfolio import Portfolio

app = Flask(__name__)
portfolio = Portfolio()

@app.route("/")
def home():
    return jsonify({
        "capital": portfolio.capital,
        "pnl": portfolio.daily_pnl,
        "positions": portfolio.positions
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
