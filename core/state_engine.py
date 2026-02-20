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

import json
import sqlite3
import os
import threading
import time

STATE_FILE = "system_state.json"
DB_FILE = "system_history.db"

_lock = threading.Lock()


class StateEngine:
    def __init__(self):
        self.state = {
            "mode": "PAPER",
            "risk_enabled": True,
            "autonomous": False,
            "capital_allocation": 50,
            "capital": 50,   # 🔥 add this line
            "last_regime": "UNKNOWN",
            "drawdown_today": 0.0,
        }

        self._init_db()
        self.load_state()
        self._auto_save()

    # -------------------
    # JSON STATE
    # -------------------

    def load_state(self):
        if os.path.exists(STATE_FILE):
            with open(STATE_FILE, "r") as f:
                self.state.update(json.load(f))

    def save_state(self):
        with _lock:
            with open(STATE_FILE, "w") as f:
                json.dump(self.state, f, indent=4)

    def _auto_save(self):
        def loop():
            while True:
                time.sleep(60)
                self.save_state()

        threading.Thread(target=loop, daemon=True).start()

    # -------------------
    # SQLITE LOGGING
    # -------------------

    def _init_db(self):
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()

        c.execute("""
        CREATE TABLE IF NOT EXISTS regime_history (
            timestamp TEXT,
            regime TEXT
        )
        """)

        conn.commit()
        conn.close()

    def log_regime(self, regime):
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute("INSERT INTO regime_history VALUES (datetime('now'), ?)", (regime,))
        conn.commit()
        conn.close()


state_engine = StateEngine()