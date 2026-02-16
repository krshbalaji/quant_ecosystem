import os
import random
from core.assimilation_engine import AssimilationEngine
from core.performance_tracker import PerformanceTracker

class RDEngine:

    def __init__(self):

        self.assimilator = AssimilationEngine()
        self.tracker = PerformanceTracker()

        self.strategy_dir = "strategies"

    def discover(self):

        # future: connect YouTube, GitHub, etc
        print("R&D: scanning for new strategy ideas")

    def generate(self):

        base_strategies = os.listdir(self.strategy_dir)

        if not base_strategies:
            return

        parent = random.choice(base_strategies)

        print(f"R&D: mutating {parent}")

        # simple mutation placeholder
        content = "RSI BUY SELL strategy"

        self.assimilator.assimilate(content)

    def evaluate(self):

        print("R&D: evaluating strategies")

        for file in os.listdir(self.strategy_dir):

            name = file.replace(".py","")

            score = self.tracker.get_score(name)

            print(name, score)

    def evolve(self):

        self.discover()

        self.generate()

        self.evaluate()
