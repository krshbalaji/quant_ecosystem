from core.portfolio import Portfolio
import random

p = Portfolio()

for _ in range(50):
    p.record_trade(random.randint(-500, 800))

print("Sharpe:", p.get_sharpe())
print("Drawdown:", p.get_drawdown())
print("Win rate:", p.get_win_rate())
print("Volatility:", p.get_volatility())
print("Trades:", p.get_trade_count())
