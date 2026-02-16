from broker.fyers_paper import FyersPaperBroker
from core.execution_simulator import ExecutionSimulator
from core.position_manager import PositionManager


class PaperTradingEngine:

    def __init__(self):

        self.broker = FyersPaperBroker()
        self.executor = ExecutionSimulator(self.broker)
        self.position_manager = PositionManager()

    def execute_decision(self, decision):

        order = self.executor.execute(decision)

        self.position_manager.update(
            self.broker.get_positions()
        )

        return order

    def get_positions(self):
        return self.position_manager.get_positions()

    def get_orders(self):
        return self.broker.get_orders()

class PaperEngine:

    def __init__(self):
        self.positions = []
        self.cash = 100000

    def on_tick(self, tick):

        price = tick["price"]

        # Simple demo logic
        if price % 10 == 0:
            self.buy(price)

    def buy(self, price):

        self.positions.append(price)
        self.cash -= price

        print(f"PAPER BUY @ {price}")
        print(f"Cash: {self.cash}")

    	