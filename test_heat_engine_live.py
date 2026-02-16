from core.portfolio import Portfolio
from core.portfolio_heat_engine import PortfolioHeatEngine
from engine.fyers_broker import FyersBroker

portfolio = Portfolio()

portfolio.update_position("NSE:RELIANCE-EQ", 5, 2500)

broker = FyersBroker()

engine = PortfolioHeatEngine(portfolio, broker)

heat = engine.calculate_heat()

print("Portfolio Heat:", heat)
