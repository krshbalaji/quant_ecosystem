import yaml
import schedule
import time
from datetime import datetime

from data.downloader import HistoricalDownloader
from core.broker_fyers import FyersBroker
from core.risk_manager import RiskManager
from core.portfolio import Portfolio
from strategies.orb_strategy import ORBStrategy
from tools.morning_health import run_health_check
from engine.portfolio_manager import PortfolioManager
from core.rd_engine import RDEngine
from core.broker_loader import load_broker
from core.maintenance import run_daily, should_run
from core.mode_controller import enforce_mode

mode = enforce_mode()

if should_run():

    run_daily()

broker = load_broker()

rd = RDEngine()
rd.evolve()

schedule.every().day.at("07:00").do(run_health_check)

cfg = yaml.safe_load(open("config/settings.yaml"))

risk = RiskManager(cfg["capital"], cfg["risk"]["risk_per_trade_pct"])

pm = PortfolioManager(broker, risk)

downloader = HistoricalDownloader("CLIENT_ID", "TOKEN")

strategy = ORBStrategy()
def weekly_retrain():
    print("🧠 Retraining ML models...")
    engine.selector.retrain()
    self.risk.capital -= 5000
    if df.empty:
        return

schedule.every().wednesday.at("08:30").do(weekly_retrain)

def daily_run():

    symbol = "NSE:NIFTYBANK-INDEX"

    df = downloader.fetch(symbol, timeframe="5")

    sig, sl = strategy.signal(df)

    if sig:
        pm.execute(symbol, sig, df.close.iloc[-1], sl)



def job():
    daily_run()

schedule.every(5).minutes.do(job)

print("Engine started... Monitoring market every 5 minutes")

import datetime

while True:
    print("Checking signals at:", datetime.datetime.now())
    schedule.run_pending()
    time.sleep(300)


while True:
    schedule.run_pending()
    time.sleep(1)

