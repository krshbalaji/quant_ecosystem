import os
import random
import importlib
import time

from core.assimilation_engine import AssimilationEngine
from core.strategy_population_guard import enforce_limit


class RDEngine:

    def __init__(self):

        self.strategies_folder = "strategies"

        self.assimilator = AssimilationEngine()

        print("R&D Engine initialized")


    def evolve(self):

        print("R&D: scanning for new strategy ideas")

        strategies = self._get_strategies()

        if not strategies:
            return

        parent = random.choice(strategies)

        print(f"R&D: mutating {parent}")

        content = self._load_strategy(parent)

        if not content:
            return

        new_content = self._mutate(content)

        self.assimilator.assimilate(new_content)

        enforce_limit()

        print("R&D evolution cycle complete")


    def _get_strategies(self):

        files = []

        for f in os.listdir(self.strategies_folder):

            if f.endswith(".py") and not f.startswith("__"):

                files.append(f)

        return files


    def _load_strategy(self, filename):

        path = os.path.join(self.strategies_folder, filename)

        try:

            with open(path, "r") as f:

                return f.read()

        except:

            return None


    def _mutate(self, content):

        lines = content.split("\n")

        if len(lines) > 5:

            idx = random.randint(0, len(lines) - 1)

            lines[idx] = lines[idx]  # safe mutation placeholder

        return "\n".join(lines)

        def run(self):

            print("R&D Engine running evolution cycle")

            try:

                if hasattr(self, "scan"):
                    self.scan()

                if hasattr(self, "mutate"):
                    self.mutate()

                if hasattr(self, "evaluate"):
                    self.evaluate()

            except Exception as e:

                print("R&D Engine error:", e)
