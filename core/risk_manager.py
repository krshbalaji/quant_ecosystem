# ==========================================
# core/risk_manager.py
# Professional capital protection engine
# ==========================================

class RiskManager:

    def __init__(self, capital):

        self.start_capital = capital
        self.capital = capital

        # -------- SETTINGS ----------
        self.risk_per_trade_pct = 0.01      # 1%
        self.max_daily_loss_pct = 0.03      # 3%
        self.daily_target_pct = 0.05        # 5%
        self.max_trades = 3
        # ----------------------------

        self.trades_today = 0
        self.pnl_today = 0

    # ---------------------------------
    # Position sizing
    # ---------------------------------
    def position_size(self, entry, stop):

        risk_amount = self.capital * self.risk_per_trade_pct
        risk_per_unit = abs(entry - stop)

        if risk_per_unit == 0:
            return 0

        qty = int(risk_amount / risk_per_unit)

        return max(qty, 1)

    # ---------------------------------
    # Can take new trade?
    # ---------------------------------
    def can_trade(self):

        if self.trades_today >= self.max_trades:
            return False

        if self.pnl_today <= -self.capital * self.max_daily_loss_pct:
            return False

        if self.pnl_today >= self.capital * self.daily_target_pct:
            return False

        return True

    # ---------------------------------
    # Update after trade
    # ---------------------------------
    def update(self, pnl):

        self.pnl_today += pnl
        self.capital += pnl
        self.trades_today += 1

    # ---------------------------------
    # Reset daily
    # ---------------------------------
    def reset_day(self):
        self.trades_today = 0
        self.pnl_today = 0
