class PaperBroker:

    def __init__(self):
        self.position = None
        self.trade_log = []

    def execute(self, signal, price):
        if signal == "BUY":
            self.position = "LONG"
            self.trade_log.append(("BUY", price))
            return f"📈 PAPER BUY at {price}"

        elif signal == "SELL":
            self.position = "SHORT"
            self.trade_log.append(("SELL", price))
            return f"📉 PAPER SELL at {price}"

        return None