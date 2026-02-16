import time
import os

from datetime import datetime
from core.health_engine import HealthEngine
from engine.modes.selected_mode import SelectedMode
from engine.modes.systematic_mode import SystematicMode
from engine.modes.swing_mode import SwingMode
from engine.ml_selector import MLSelector
from engine.fyers_broker import FyersBroker
from engine.telegram_notifier import TelegramNotifier
from core.portfolio import Portfolio
from core.risk_manager import RiskManager
from dashboard.web_dashboard import update_data
from core.drawdown_guard import DrawdownGuard
from core.kill_switch import KillSwitch
from engine.mode_engine import ModeEngine

self.dd_guard = DrawdownGuard(max_dd=0.20)
self.kill_switch = KillSwitch(daily_loss_limit=0.05)
funds = self.broker.get_available_funds()
self.risk.update_capital(funds)
self.health = HealthEngine(self.portfolio)


class Engine:

    def __init__(self):

        print("🚀 Initializing engine...")
        
        self.mode_name = "selected"   # default
        self.mode = self._create_mode(self.mode_name)
        
        health_status = self.health.evaluate()
        print("System Health:", health_status)

        self.health_engine = SystemHealth()
        self.mode_engine = ModeEngine()
        self.current_mode = "BALANCED"

        self.mode = "auto"  # or "manual"

        self.selector = MLSelector(
            self.broker.get_trade_history
    )

        self.ml_selector = MLSelector(self.strategy_selector.get_all())

        best, ranking = self.selector.rank(self.strategy_stats_df)

        print(f"🤖 ML Selected Strategy: {best}")

        self.strategy_selector.activate(best)
    
        if self.mode == "auto":
            chosen = self.selector.select()
            print(f"🧠 ML selected strategy: {chosen}")
            strategy = self.strategy_selector.get(chosen)
        else:
            strategy = self.strategy_selector.get(self.config["strategy"])

    def auto_select_strategy(self):

        best = self.ml_selector.select()

        self.strategy_selector.set_active(best)
        metrics = {
            "rolling_sharpe": self.portfolio.get_sharpe(),
            "drawdown": self.portfolio.get_drawdown(),
            "ml_confidence": self.ml_selector.get_confidence(),
            "win_rate": self.portfolio.get_win_rate(),
            "volatility": self.portfolio.get_volatility()
        }

        health_score = self.health_engine.calculate(metrics)
        self.current_mode = self.mode_engine.decide(health_score)

        print(f"🧠 System Health: {health_score} | Mode: {self.current_mode}")

        self.telegram.notify(
            f"🧠 ML selected strategy → {best.name}"
        )

        name, score = self.selector.select()

        self.current_strategy = name
        self.ml_confidence = round(score * 100, 2)

        If system_confidence > threshold:
            REAL all days
        Else:
            Wednesday only REAL

        equity = self.risk.capital

        health_status = self.health.evaluate()

        if health_status == "HEALTHY":
            risk_multiplier = 1.0
        elif health_status == "CAUTION":
            risk_multiplier = 0.5
        else:
            risk_multiplier = 0.2

        available_funds = self.broker.get_available_funds()

        risk_capital = available_funds * 0.02 * risk_multiplier

        lot_size = int(risk_capital / price_per_lot)

        def allocate_capital(self):
            health = self.health_engine.score
            confidence = self.ml_confidence

            if health > 80 and confidence > 70:
                multiplier = 1.0
            elif health > 60:
                multiplier = 0.6
            else:
                multiplier = 0.3

            return self.base_capital * multiplier

        # Drawdown check
        if not self.dd_guard.update(equity):
            print("🛑 Max drawdown hit. Stopping engine.")
            return

        if self.risk.check_drawdown():
            self.mode = "PAPER"
            print("⚠ Switched to PAPER due to drawdown")

        if portfolio.get_drawdown() < -0.08:
            self.close_all_positions()

        # Daily kill switch
        if self.kill_switch.check(equity):
            print("🚨 Daily loss limit hit. No more trades today.")
            return
        
        self.rankings = self.ranker.rank(self.strategy_stats)
        self.current_strategy = self.rankings[0]["name"]

        health = self.health.evaluate()

        if health == "CRITICAL":
            print("🚨 Kill Switch Activated")
            self.close_all_positions()
            return

        # =========================
        # Broker
        # =========================
        self.broker = FyersBroker(
            os.getenv("FYERS_CLIENT_ID"),
            os.getenv("FYERS_ACCESS_TOKEN")
        )
        
        if self.trade_mode == "paper":
            self.paper_execute(order)
        else:
            self.real_execute(order)

        # =========================
        # Telegram
        # =========================
        self.tg = TelegramNotifier()
        self.tg.send(f"PnL: ₹{self.pnl} | Trades: {self.trade_count}")
        if chosen != self.current_strategy:
            if chosen != self.current_strategy:
        self.telegram.send(
            f"Strategy switched → {self.current_strategy}\n"
            f"Mode: {self.trade_mode}\n"
            f"Confidence: {self.confidence}%"
        )
        
        # =========================
        # Portfolio + Risk
        # =========================
        self.portfolio = Portfolio()
        self.risk = RiskManager(capital=100000)

        self.pnl = 0
        self.trade_count = 0

        print("✅ Broker + Telegram + Portfolio ready")
    
    def _create_mode(self, name):
        if name == "systematic":
            return SystematicMode(self)
        elif name == "swing":
            return SwingMode(self)
        return SelectedMode(self)

    def switch_mode(self, name):
        self.mode_name = name
        self.mode = self._create_mode(name)

        self.telegram.notify(f"🔁 Strategy mode switched → {name.upper()}")
        
        self.mode.run()

    regime = self.regime.detect(latest_prices)

    if regime == "trend":
        strategy = "trend_following"

    elif regime == "sideways":
        strategy = "mean_reversion"

    elif regime == "volatile":
        strategy = "options_hedge"

    def get_drawdown_curve(self):
        equity = self.get_equity_curve()
        peak = equity.cummax()
        drawdown = (equity - peak) / peak
        return drawdown.tolist()

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
        schedule.every().day.at("09:10").do(self.auto_select_strategy)

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
                self.telegram.notify(
                    f"✅ Trade executed\n{symbol} {side} Qty:{qty}"
                )
                
                self.telegram.notify("🚨 Daily loss hit. Trading paused.")

                # --------------------------------
                # Update dashboard LIVE
                # --------------------------------
                update_data(
                    self.pnl,
                    self.trade_count,
                    self.risk.capital,
                    self.current_regime,
                    self.trade_mode,
                    self.confidence
            )


                print(f"📊 PnL: {self.pnl} | Trades: {self.trade_count}")

            except Exception as e:
                print("⚠ Engine error:", e)

            time.sleep(5)


# ======================================
# STARTER
# ======================================
def start():
    Engine().run()
