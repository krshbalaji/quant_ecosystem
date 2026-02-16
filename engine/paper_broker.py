import random
from datetime import datetime


class PaperBroker:

    def __init__(self):
        print("PAPER Broker Connected")

        self.positions = {}
        self.orders = {}
        self.order_count = 0

    # --------------------------------------------------
    # Dynamic live-like price generator
    # --------------------------------------------------

    def get_quote(self, symbol):

        # realistic price ranges
        base_prices = {
            "RELIANCE": 2400,
            "TCS": 3800,
            "INFY": 1500,
            "HDFCBANK": 1650,
            "ICICIBANK": 1050,
            "NIFTY": 22000
        }

        base = base_prices.get(symbol, 1000)

        # simulate market movement
        variation = random.uniform(-1.5, 1.5)

        price = round(base * (1 + variation / 100), 2)

        return price


    # --------------------------------------------------
    # Place order dynamically
    # --------------------------------------------------

    def place_order(self, symbol, side, qty):

        price = self.get_quote(symbol)

        self.order_count += 1

        order_id = f"PAPER_{self.order_count}"

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        order = {
            "order_id": order_id,
            "symbol": symbol,
            "side": side,
            "qty": qty,
            "price": price,
            "status": "FILLED",
            "timestamp": timestamp
        }

        self.orders[order_id] = order

        self._update_position(symbol, side, qty, price)

        return order


    # --------------------------------------------------
    # Update position
    # --------------------------------------------------

    def _update_position(self, symbol, side, qty, price):

        pos = self.positions.get(symbol, {"qty": 0, "avg_price": 0})

        if side == "BUY":

            new_qty = pos["qty"] + qty

            if new_qty != 0:
                new_avg = (
                    (pos["qty"] * pos["avg_price"]) +
                    (qty * price)
                ) / new_qty
            else:
                new_avg = 0

        else:
            new_qty = pos["qty"] - qty
            new_avg = pos["avg_price"]

        self.positions[symbol] = {
            "qty": new_qty,
            "avg_price": round(new_avg, 2)
        }


    # --------------------------------------------------
    # Return positions
    # --------------------------------------------------

    def get_positions(self):

        return self.positions


    # --------------------------------------------------
    # Return orders
    # --------------------------------------------------

    def get_orders(self):

        return self.orders
