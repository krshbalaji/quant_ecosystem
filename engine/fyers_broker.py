# ======================================================
# engine/fyers_broker.py
# LIVE FYERS EXECUTION BROKER
# ======================================================

import requests
from core.logger import log


class FyersBroker:

    def __init__(self, webhook_url):
        self.webhook = webhook_url

    # ---------------------------------
    def place_order(self, side, symbol, qty, price, sl=None, tp=None):

        payload = {
            "broker": "FYERS",
            "mode": "LIVE",
            "symbol": symbol,
            "side": side,
            "qty": qty,
            "price": price,
            "sl": sl,
            "tp": tp
        }

        try:
            r = requests.post(self.webhook, json=payload, timeout=5)
            log(f"📡 FYERS ORDER SENT -> {payload}")

        except Exception as e:
            log(f"❌ FYERS ERROR: {e}")
