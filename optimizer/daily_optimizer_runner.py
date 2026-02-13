import schedule
import time
from optimizer.walkforward_optimizer import WalkForwardOptimizer
from optimizer.strategy_loader import load_strategies


def job():
    strategies = load_strategies()
    opt = WalkForwardOptimizer(strategies)
    opt.run()


schedule.every().day.at("08:45").do(job)

print("📅 Optimizer scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(30)
