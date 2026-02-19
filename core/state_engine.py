import threading

class StateEngine:
    def __init__(self):
        self.lock = threading.Lock()
        self.mode = "PAPER"
        self.autonomous = True
        self.active_strategy = None
        self.regime = "UNKNOWN"

    def set_mode(self, mode):
        with self.lock:
            self.mode = mode

    def set_strategy(self, name):
        with self.lock:
            self.active_strategy = name

    def set_regime(self, regime):
        with self.lock:
            self.regime = regime

    def toggle_autonomy(self):
        with self.lock:
            self.autonomous = not self.autonomous

    def snapshot(self):
        with self.lock:
            return {
                "mode": self.mode,
                "autonomous": self.autonomous,
                "strategy": self.active_strategy,
                "regime": self.regime
            }

state_engine = StateEngine()
