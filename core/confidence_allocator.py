import json
import os


PERFORMANCE_FILE = "data/performance.json"


class ConfidenceAllocator:

    def __init__(self):

        print("Confidence Allocator initialized")


    def allocate(self, total_capital):

        scores = self.load_scores()

        if not scores:
            return {}

        positive = {
            k: v for k, v in scores.items()
            if v > 0
        }

        total_score = sum(positive.values())

        allocation = {}

        for strategy, score in positive.items():

            weight = score / total_score

            allocation[strategy] = total_capital * weight

        return allocation


    def load_scores(self):

        if not os.path.exists(PERFORMANCE_FILE):
            return {}

        with open(PERFORMANCE_FILE) as f:
            return json.load(f)
