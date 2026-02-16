import time


class GuardLayer:

    def __init__(self):

        self.max_position_size = 100
        self.max_order_size = 20
        self.max_daily_loss = -5000

        self.daily_pnl = 0
        self.trade_count = 0

        print("Guard Layer Activated")


    def approve_order(self, symbol, side, qty, current_position):

        # Rule 1: Prevent oversized order
        if qty > self.max_order_size:
            return False, "Order exceeds max order size"

        # Rule 2: Prevent oversized position
        projected_position = current_position + qty if side == "BUY" else current_position - qty

        if abs(projected_position) > self.max_position_size:
            return False, "Position exceeds max allowed size"

        # Rule 3: Daily loss protection
        if self.daily_pnl <= self.max_daily_loss:
            return False, "Daily loss limit exceeded"

        # Rule 4: Trade frequency protection
        if self.trade_count > 500:
            return False, "Trade frequency exceeded"

        self.trade_count += 1

        return True, "Approved"


    def update_pnl(self, pnl):

        self.daily_pnl += pnl


    def reset_daily(self):

        self.daily_pnl = 0
        self.trade_count = 0
