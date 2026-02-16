import time
import threading
from datetime import datetime

# Replace later with real FYERS connection
class LiveFeedEngine:

    def __init__(self):
        self.running = False
        self.price = 0
        self.listeners = []

    def connect(self):
        print("Live Feed Engine Connected")
        self.running = True
        threading.Thread(target=self._feed_loop, daemon=True).start()

    def _feed_loop(self):
        while self.running:
            # Simulated live price (replace with FYERS)
            self.price += 1

            tick = {
                "symbol": "NIFTY",
                "price": self.price,
                "time": datetime.now().isoformat()
            }

            self._notify(tick)

            time.sleep(1)

    def _notify(self, tick):
        for listener in self.listeners:
            listener(tick)

    def subscribe(self, callback):
        self.listeners.append(callback)

    def stop(self):
        self.running = False
        print("Live Feed Stopped")
