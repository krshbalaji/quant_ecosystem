from core.performance_tracker import PerformanceTracker

self.tracker = PerformanceTracker()

def select_best(self, available_strategies):

    scored = []

    for s in available_strategies:

        score = self.tracker.get_score(s.name)

        scored.append((s, score))

    scored.sort(key=lambda x: x[1], reverse=True)

    return scored[0][0]


def choose_best_strategy(regime, ml_confidence):
    if regime == "trend" and ml_confidence > 0.6:
        return "Breakout"
    elif regime == "sideways":
        return "MeanReversion"
    else:
        return "OptionsPremium"
