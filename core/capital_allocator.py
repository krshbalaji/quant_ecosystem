import math
from datetime import datetime


class CapitalAllocator:

    def __init__(self, capital=100000.0, risk_per_trade=0.02):
        """
        capital: total trading capital
        risk_per_trade: % risk per trade (default 2%)
        """

        self.capital = float(capital)
        self.risk_per_trade = float(risk_per_trade)

        print(f"CapitalAllocator initialized with capital: {self.capital}")

   
    def adaptive_allocation(self, strategy_score):

       base = self.capital * 0.02

       multiplier = 0.5 + strategy_score

       return base * multiplier


    # ---------------------------------------------------
    # Calculate quantity based on entry and stop
    # ---------------------------------------------------

    def calculate_qty(self, price, risk_per_trade=0.02):

        if price <= 0:
            return 0

        risk_capital = self.capital * risk_per_trade

        qty = int(risk_capital / price)

        return max(qty, 1)

    # ---------------------------------------------------
    # Reduce capital after trade (optional future use)
    # ---------------------------------------------------

    def update_capital(self, pnl):

        self.capital += pnl

        print(
            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
            f"Capital updated: {self.capital}"
        )
