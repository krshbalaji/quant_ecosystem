# ======================================================
# engine/paper_broker.py
# Paper Trading Broker Simulator
# ======================================================

from core.logger import log


class PaperBroker:

    def __init__(self):
        self.trades = []

    def buy(self, symbol, qty, price):
        log(f"[PAPER BUY] {symbol} Qty={qty} @ {price}")
        self.trades.append(("BUY", symbol, qty, price))

    def sell(self, symbol, qty, price):
        log(f"[PAPER SELL] {symbol} Qty={qty} @ {price}")
        self.trades.append(("SELL", symbol, qty, price))
