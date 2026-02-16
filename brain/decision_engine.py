import random

class DecisionEngine:

    def generate_decision(self):

        symbol = random.choice([
            "NIFTY",
            "BANKNIFTY",
            "RELIANCE"
        ])

        side = random.choice([
            "BUY",
            "SELL"
        ])

        qty = random.randint(1, 10)

        return {
            "symbol": symbol,
            "side": side,
            "qty": qty
        }
