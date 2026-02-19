import time
import threading

class PerformanceTracker:

    def __init__(self):
        self.equity = 8000
        self.history = []
        self.lock = threading.Lock()

        threading.Thread(target=self._loop, daemon=True).start()

    def _loop(self):
        while True:
            with self.lock:
                self.history.append({
                    "timestamp": time.time(),
                    "equity": self.equity
                })
            time.sleep(10)

    def update_equity(self, new_equity):
        with self.lock:
            self.equity = new_equity

    def get_snapshot(self):
        with self.lock:
            return {
                "equity": self.equity,
                "history": self.history[-100:]
            }

performance_tracker = PerformanceTracker()

def get_performance_snapshot():
    return performance_tracker.get_snapshot()
