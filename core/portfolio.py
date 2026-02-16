# core/portfolio.py

import time

class Portfolio:

    def __init__(self, starting_capital=100000):

        self.starting_capital = starting_capital
        self.cash = starting_capital

        # symbol → {qty, avg_price}
        self.positions = {}

        # symbol → live price
        self.market_prices = {}

        self.trade_log = []


    # -----------------------------
    # POSITION UPDATE (CRITICAL)
    # -----------------------------
    def update_position(self, symbol, qty, price):

        if symbol not in self.positions:

            self.positions[symbol] = {
                "qty": qty,
                "avg_price": price
            }

        else:

            pos = self.positions[symbol]

            total_qty = pos["qty"] + qty

            if total_qty == 0:

                del self.positions[symbol]

            else:

                pos["avg_price"] = (
                    (pos["qty"] * pos["avg_price"]) + (qty * price)
                ) / total_qty

                pos["qty"] = total_qty

        self.cash -= qty * price

        self.trade_log.append({
            "symbol": symbol,
            "qty": qty,
            "price": price,
            "timestamp": time.time()
        })


    # -----------------------------
    # LIVE MARKET PRICE UPDATE
    # -----------------------------
    def update_market_price(self, symbol, price):

        self.market_prices[symbol] = price


    # -----------------------------
    # PORTFOLIO VALUE
    # -----------------------------
    def total_value(self):

        value = self.cash

        for symbol, pos in self.positions.items():

            market_price = self.market_prices.get(symbol, pos["avg_price"])

            value += pos["qty"] * market_price

        return value


    # -----------------------------
    # PORTFOLIO HEAT
    # -----------------------------
    def portfolio_heat(self):

        exposure = 0

        total_value = self.total_value()

        if total_value == 0:
            return 0

        for symbol, pos in self.positions.items():

            market_price = self.market_prices.get(symbol, pos["avg_price"])

            exposure += abs(pos["qty"] * market_price)

        return exposure / total_value


    # -----------------------------
    # GET POSITIONS
    # -----------------------------
    def get_positions(self):

        return self.positions


    # -----------------------------
    # GET CASH
    # -----------------------------
    def get_cash(self):

        return self.cash
    # ==========================================
# Drawdown calculation for Risk Manager
# ==========================================

def drawdown(equity_curve):
    """
    Calculate maximum drawdown from equity curve
    """
    if equity_curve is None or len(equity_curve) == 0:
        return 0.0

    peak = equity_curve[0]
    max_drawdown = 0.0

    for value in equity_curve:
        if value > peak:
            peak = value

        current_drawdown = (peak - value) / peak

        if current_drawdown > max_drawdown:
            max_drawdown = current_drawdown

    return max_drawdown

