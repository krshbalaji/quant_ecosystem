import time
import os
from datetime import datetime

from engine.fyers_broker import FyersBroker
from engine.telegram_notifier import TelegramNotifier
from engine.portfolio import Portfolio
from core.risk_manager import RiskManager
from dashboard.web_dashboard import update_data


class Engine:

    def __init__(self):

        print("🚀 Initializing engine...")

        # =========================
        # Broker
        # =========================
        self.broker = FyersBroker(
            os.getenv("FYERS_CLIENT_ID"),
            os.getenv("FYERS_ACCESS_TOKEN")
        )

        # =========================
        # Telegram
        # =========================
        self.tg = TelegramNotifier()

        # =========================
        # Portfolio + Risk
        # =========================
        self.portfolio = Portfolio()
        self.risk = RiskManager(capital=100000)

        self.pnl = 0
        self.trade_count = 0

        print("✅ Broker + Telegram + Portfolio ready")

    # =============================
    # Market hours check
    # =============================
    def market_open(self):
        now = datetime.now().time()
        return now >= datetime.strptime("09:15", "%H:%M").time() and \
               now <= datetime.strptime("15:30", "%H:%M").time()

    # =============================
    # MAIN LOOP
    # =============================
    def run(self):

        print("🚀 Engine loop started")

        while True:

            if not self.market_open():
                print("⏰ Market closed. Sleeping 60s")
                time.sleep(60)
                continue

            try:

                # --------------------------------
                # Pull trade history from Fyers
                # --------------------------------
                trades = self.broker.get_trade_history()

                self.pnl = sum([t.get("pnl", 0) for t in trades])
                self.trade_count = len(trades)

                # --------------------------------
                # Update dashboard LIVE
                # --------------------------------
                update_data(self.pnl, self.trade_count, self.risk.capital, self.positions, self.orders)

                print(f"📊 PnL: {self.pnl} | Trades: {self.trade_count}")

            except Exception as e:
                print("⚠ Engine error:", e)

            time.sleep(5)


# ======================================
# STARTER
# ======================================
def start():
    Engine().run()
