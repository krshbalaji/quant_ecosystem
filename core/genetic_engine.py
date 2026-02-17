import os
import random


class GeneticEngine:

    def __init__(self):

        self.dir = "strategies"


    def breed(self):

        strategies = [

            f for f in os.listdir(self.dir)

            if f.endswith(".py")
        ]

        if len(strategies) < 2:

            return

        parent1, parent2 = random.sample(strategies, 2)

        with open(f"{self.dir}/{parent1}") as f1:

            code1 = f1.readlines()

        with open(f"{self.dir}/{parent2}") as f2:

            code2 = f2.readlines()

        split1 = len(code1) // 2

        split2 = len(code2) // 2

        child_code = code1[:split1] + code2[split2:]

        child_name = f"genetic_{random.randint(10000,99999)}.py"

        with open(f"{self.dir}/{child_name}", "w") as f:

            f.writelines(child_code)

        print(f"Genetic Engine created offspring: {child_name}")
