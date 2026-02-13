from strategies.vwap_pullback import VWAPPullback
from strategies.ema_ribbon import EMARibbon


def load_strategies():
    return [
        VWAPPullback,
        EMARibbon
    ]
