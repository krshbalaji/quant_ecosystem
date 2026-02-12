# ===============================================
# engine/runner.py
# FULL PROFESSIONAL TRADING ENGINE (FINAL)
# ===============================================

import datetime
import time
from engine.fyers_broker import FyersBroker
from engine.telegram_notifier import Telegram
from engine.portfolio_manager import PortfolioManager
from options.options_engine import OptionsEngine

from core.logger import log
from core.risk_manager import RiskManager


# =========================================================
# CONFIG
# =========================================================

CAPITAL = 8000

TRAILING_MULTIPLIER = 1.5      # trail after 1.5R
BREAKEVEN_MULTIPLIER = 1.0     # move to BE at 1R

SLEEP_SECONDS = 5


# =========================================================
# ENGINE
# =========================================================

class TradingEngine:

    def __init__(self, strategy):

        self.strategy = strategy

        self.risk = RiskManager(CAPITAL)

        self.position = None
        self.entry = None
        self.stop = None
        self.target = None
        self.qty = 0

    self.current_day = None
    self.broker = FyersBroker("YOUR_WEBHOOK_URL")
    self.telegram = Telegram("YOUR_BOT_TOKEN", "YOUR_CHAT_ID")
    self.options = OptionsEngine(self.broker)

    self.portfolio = PortfolioManager(8000)


    # =====================================================
    # MARKET HOURS CONTROL
    # =====================================================

    def market_open(self):
        now = datetime.datetime.now().time()
        return now >= datetime.time(9, 15) and now <= datetime.time(15, 25)


    # =====================================================
    # DAILY RESET
    # =====================================================

    def reset_day(self):
        self.risk.reset_day()
        self.position = None
        log("🔄 New Day Reset")


    # =====================================================
    # ENTRY LOGIC
    # =====================================================

    def open_position(self, side, price, stop_price):

        if not self.risk.can_trade():
            log("🚫 Risk Manager blocked trading")
            return

        self.entry = price
        self.stop = stop_price

        risk_per_unit = abs(price - stop_price)

        self.qty = self.risk.position_size(price, stop_price)

        self.target = price + (risk_per_unit * 2) if side == "BUY" else price - (risk_per_unit * 2)

        self.position = side

        log(f"✅ ENTRY {side} | Qty={self.qty} | Entry={price} | Stop={stop_price} | Target={self.target}")
	# 🔥 SEND TO FYERS
    opt_symbol = self.options.execute(symbol, side, price, qty)

	# 🔔 TELEGRAM
    self.telegram.send(f"ENTRY {side} {self.strategy.symbol} Qty={self.qty} @ {price}")


    # =====================================================
    # TRAILING + BREAKEVEN
    # =====================================================

    def manage_position(self, price):

        if self.position is None:
            return

        risk_unit = abs(self.entry - self.stop)

        profit_move = abs(price - self.entry)

        # -------------------------
        # BREAKEVEN
        # -------------------------
        if profit_move >= risk_unit * BREAKEVEN_MULTIPLIER:

            if self.position == "BUY":
                self.stop = max(self.stop, self.entry)
            else:
                self.stop = min(self.stop, self.entry)

            log("🟡 Stop moved to Breakeven")

        # -------------------------
        # TRAILING STOP
        # -------------------------
        if profit_move >= risk_unit * TRAILING_MULTIPLIER:

            trail = risk_unit * 0.5

            if self.position == "BUY":
                self.stop = max(self.stop, price - trail)
            else:
                self.stop = min(self.stop, price + trail)

            log(f"🔵 Trailing Stop Updated -> {self.stop}")

        # -------------------------
        # EXIT CHECK
        # -------------------------
        exit_trade = False

        if self.position == "BUY":
            if price <= self.stop or price >= self.target:
                exit_trade = True
        else:
            if price >= self.stop or price <= self.target:
                exit_trade = True

        if exit_trade:
            self.close_position(price)


    # =====================================================
    # EXIT
    # =====================================================

    def close_position(self, exit_price):

        if self.position is None:
            return

        pnl = (exit_price - self.entry) * self.qty

        if self.position == "SELL":
            pnl = -pnl

        self.risk.update(pnl)

        log(f"❌ EXIT | PnL={pnl:.2f} | Capital={self.risk.capital:.2f}")
    self.telegram.send(f"EXIT {self.strategy.symbol} | PnL={pnl:.2f}")

    self.position = None


    # =====================================================
    # MAIN LOOP
    # =====================================================

    def start(self):

        log("🚀 Trading Engine Started")

        while True:

            today = datetime.date.today()

            if self.current_day != today:
                self.current_day = today
                self.reset_day()

            if not self.market_open():
                time.sleep(SLEEP_SECONDS)
                continue

            price = self.strategy.get_price()

            signal = self.strategy.get_signal()

            # -------------------------
            # ENTRY
            # -------------------------
            if self.position is None and signal:

                side, stop_price = signal
                self.open_position(side, price, stop_price)

            # -------------------------
            # MANAGEMENT
            # -------------------------
            else:
                self.manage_position(price)

            time.sleep(SLEEP_SECONDS)
# =====================================================
# ENTRY POINT
# =====================================================

def start():
    from strategies.sample_strategy import SampleStrategy   # temp strategy

    strategy = SampleStrategy()
    engine = TradingEngine(strategy)
    engine.start()
