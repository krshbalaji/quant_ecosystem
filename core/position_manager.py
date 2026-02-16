class PositionManager:

    def __init__(self):
        self.positions = {}

    def update(self, broker_positions):
        self.positions = broker_positions

    def get_exposure(self):
        exposure = 0
        for symbol, pos in self.positions.items():
            exposure += abs(pos["qty"] * pos["avg_price"])
        return exposure

    def get_positions(self):
        return self.positions
