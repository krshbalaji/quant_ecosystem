# ======================================
# SIMPLE PORTFOLIO MANAGER
# ======================================

from core.logger import log


class Portfolio:

    def __init__(self):
        self.positions = {}

    # ---------------------------
    # Add position
    # ---------------------------
    def add(self, symbol, qty, price):

        self.positions[symbol] = {
            "qty": qty,
            "price": price
        }

        log(f"Portfolio ADD → {symbol} {qty} @ {price}")

    # ---------------------------
    # Remove position
    # ---------------------------
    def remove(self, symbol):

        if symbol in self.positions:
            del self.positions[symbol]
            log(f"Portfolio REMOVE → {symbol}")

    # ---------------------------
    # Check
    # ---------------------------
    def has(self, symbol):
        return symbol in self.positions

    # ---------------------------
    # Get
    # ---------------------------
    def get(self, symbol):
        return self.positions.get(symbol)

    # ---------------------------
    # All
    # ---------------------------
    def all(self):
        return self.positions
