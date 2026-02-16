import random
import time

class FyersPaperBroker:
    def __init__(self):
        self.orders = {}
        self.positions = {}
        self.order_id_counter = 1

    def place_order(self, symbol, side, qty, price=None):
        order_id = f"PAPER_{self.order_id_counter}"
        self.order_id_counter += 1

        fill_price = price if price else self._get_market_price(symbol)

        order = {
            "order_id": order_id,
            "symbol": symbol,
            "side": side,
            "qty": qty,
            "price": fill_price,
            "status": "FILLED",
            "timestamp": time.time()
        }

        self.orders[order_id] = order
        self._update_position(symbol, side, qty, fill_price)

        return order

    def _get_market_price(self, symbol):
        return round(100 + random.uniform(-5, 5), 2)

    def _update_position(self, symbol, side, qty, price):

        if symbol not in self.positions:
            self.positions[symbol] = {
                "qty": 0,
                "avg_price": 0
            }

        pos = self.positions[symbol]

        if side == "BUY":
            new_qty = pos["qty"] + qty
            pos["avg_price"] = (
                (pos["qty"] * pos["avg_price"] + qty * price)
                / new_qty
            )
            pos["qty"] = new_qty

        elif side == "SELL":
            pos["qty"] -= qty

    def get_positions(self):
        return self.positions

    def get_orders(self):
        return self.orders
