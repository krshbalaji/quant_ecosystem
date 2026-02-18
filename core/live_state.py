# core/live_state.py

from datetime import datetime
import random

live_state = {
    "equity": 8000,
    "regime": "UNKNOWN",
    "mode": "PAPER",
    "last_strategy": "None",
    "trades_today": 0,
    "win_rate": 0,
    "drawdown": 0,
    "timestamp": datetime.now().strftime("%H:%M:%S")
}

def update_state(**kwargs):
    for k, v in kwargs.items():
        live_state[k] = v
