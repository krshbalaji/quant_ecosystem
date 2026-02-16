class PortfolioHeatEngine:

    def __init__(self, portfolio, broker):

        self.portfolio = portfolio
        self.broker = broker

    def calculate_heat(self):

        total_heat = 0

        for symbol, position in self.portfolio.positions.items():

            qty = position["qty"]
            avg_price = position["avg_price"]

            live_price = self.broker.get_quote(symbol)

            pnl = (live_price - avg_price) * qty

            exposure = abs(qty * live_price)

            heat = exposure * 0.01

            total_heat += heat

        return total_heat
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
