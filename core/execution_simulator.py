class ExecutionSimulator:

    def __init__(self, broker):
        self.broker = broker

    def execute(self, decision):

        symbol = decision["symbol"]
        side = decision["side"]
        qty = decision["qty"]

        order = self.broker.place_order(
            symbol=symbol,
            side=side,
            qty=qty
        )

        return order
