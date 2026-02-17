import os
import json
import shutil

PERFORMANCE_FILE = "data/performance.json"
STRATEGY_DIR = "strategies"

MAX_POPULATION = 30
MIN_POPULATION = 10

ELITE_PERCENT = 0.30
KILL_PERCENT = 0.40


class PopulationManager:

    def __init__(self):

        print("Population Manager initialized")


    def run(self):

        try:

            scores = self.load_scores()

            if not scores:
                return

            ranked = sorted(
                scores.items(),
                key=lambda x: x[1],
                reverse=True
            )

            total = len(ranked)

            elite_count = int(total * ELITE_PERCENT)

            kill_count = int(total * KILL_PERCENT)

            elite = ranked[:elite_count]

            weak = ranked[-kill_count:]

            self.protect_elite(elite)

            self.kill_weak(weak)

            self.enforce_population_limit()

        except Exception as e:

            print("Population manager error:", e)


    def load_scores(self):

        if not os.path.exists(PERFORMANCE_FILE):
            return {}

        with open(PERFORMANCE_FILE, "r") as f:
            return json.load(f)


    def protect_elite(self, elite):

        elite_names = [name for name, score in elite]

        with open("data/elite.json", "w") as f:
            json.dump(elite_names, f)

        print(f"Protected {len(elite_names)} elite strategies")


    def kill_weak(self, weak):

        elite = self.load_elite()

        for name, score in weak:

            if name in elite:
                continue

            path = f"{STRATEGY_DIR}/{name}.py"

            if os.path.exists(path):

                os.remove(path)

                print(f"Eliminated weak strategy: {name}")


    def load_elite(self):

        if not os.path.exists("data/elite.json"):
            return []

        with open("data/elite.json") as f:
            return json.load(f)


    def enforce_population_limit(self):

        strategies = [

            f.replace(".py", "")
            for f in os.listdir(STRATEGY_DIR)
            if f.endswith(".py")
        ]

        if len(strategies) <= MAX_POPULATION:
            return

        scores = self.load_scores()

        ranked = sorted(
            strategies,
            key=lambda x: scores.get(x, 0)
        )

        excess = len(strategies) - MAX_POPULATION

        for name in ranked[:excess]:

            path = f"{STRATEGY_DIR}/{name}.py"

            if os.path.exists(path):

                os.remove(path)

                print(f"Removed excess strategy: {name}")
