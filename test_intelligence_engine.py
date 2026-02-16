from engine.paper_broker import PaperBroker
from core.portfolio import Portfolio
from core.portfolio_heat_engine import PortfolioHeatEngine
from core.capital_allocator import CapitalAllocator
from core.intelligence_engine import IntelligenceEngine


broker = PaperBroker()

portfolio = Portfolio()

heat_engine = PortfolioHeatEngine(
    portfolio=portfolio,
    broker=broker
)

capital_allocator = CapitalAllocator(100000)

engine = IntelligenceEngine(
    broker=broker,
    portfolio=portfolio,
    heat_engine=heat_engine,
    capital_allocator=capital_allocator
)


decision = engine.approve_trade(
    symbol="RELIANCE",
    signal_strength=0.8,
    volatility=0.3,
    strategy="TREND_FOLLOWING"
)

print(decision)
