import os
import shutil
import random


class RDEngine:

    def __init__(self):

        print("R&D Engine initialized")

        self.strategy_dir = "strategies"


    def run(self):

        print("R&D Engine evolution cycle")

        try:

            self.evolve()

        except Exception as e:

            print("R&D error:", e)


    def evolve(self):

        strategies = [

            f for f in os.listdir(self.strategy_dir)

            if f.endswith(".py")
        ]

        if len(strategies) < 2:

            return

        parent1, parent2 = random.sample(strategies, 2)

        child = f"strategy_gen_{random.randint(10000,99999)}.py"

        shutil.copy(

            os.path.join(self.strategy_dir, parent1),

            os.path.join(self.strategy_dir, child)
        )

        print(f"Evolved new strategy: {child}")
