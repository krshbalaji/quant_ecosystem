# ======================================
# MASTER TRADING ENGINE (FINAL VERSION)
# ======================================

import time
import datetime
import yaml
import os

from core.logger import log
from core.risk_manager import RiskManager

from engine.fyers_broker import FyersBroker
from engine.telegram_notifier import TelegramNotifier
from engine.portfolio import Portfolio
from engine.trade_journal import TradeJournal
from engine.optimizer import Optimizer
from engine.backtester import Backtester

self.optimizer = Optimizer(None, Backtester())


# ======================================
class Engine:

    def __init__(self):

        BASE = os.path.dirname(os.path.dirname(__file__))
        cfg = yaml.safe_load(open(os.path.join(BASE, "config", "settings.yaml")))

        # ---------------------------------
        # Core modules
        # ---------------------------------
        self.broker = FyersBroker(cfg["broker"]["webhook_url"])
        self.tg = TelegramNotifier()
        self.portfolio = Portfolio()
        self.journal = TradeJournal()

        self.risk = RiskManager(cfg["capital"]["initial"])

        self.running = True

        log("Engine initialized")

    # ======================================
    # MARKET HOURS CONTROL
    # ======================================
    def market_open(self):

        now = datetime.datetime.now().time()
        return now >= datetime.time(9, 15) and now <= datetime.time(15, 30)

    # ======================================
    # PLACE ORDER WRAPPER
    # ======================================
    def place_trade(self, side, symbol, qty, price, sl=None, tp=None):

        if not self.risk.allow_trade():
            log("Risk manager blocked trade")
            return

        self.broker.place_order(side, symbol, qty, price, sl, tp)

        self.tg.send(f"{side} {symbol} @ {price} qty:{qty}")

        self.journal.log(symbol, side, qty, price, self.portfolio.capital)

    # ======================================
    # YOUR STRATEGIES HERE
    # ======================================
    def execute_strategies(self):

        log("Running strategies...")

        # ======================================
        # SAMPLE DEMO SIGNAL
        # replace with real strategy signals
        # ======================================

        symbol = "NSE_FO:BANKNIFTY-I"
        price = 50000
        qty = 1

        # example condition
        if datetime.datetime.now().second % 120 == 0:
            self.place_trade("BUY", symbol, qty, price)

    # ======================================
    # MAIN LOOP
    # ======================================
    def run(self):

        log("Engine loop started")

        while self.running:

            try:

                if not self.market_open():
                    log("Market closed. Sleeping 60s")
                    time.sleep(60)
                    continue

                self.execute_strategies()

                time.sleep(5)

            except Exception as e:

                log(f"ERROR: {e}")
                self.tg.send(f"Engine crash: {e}")
                time.sleep(5)


# ======================================
def start():
    Engine().run()
