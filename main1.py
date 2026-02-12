from data.downloader import HistoricalDownloader
from core.broker_fyers import FyersBroker
from core.risk_manager import RiskManager
from engine.portfolio_manager import PortfolioManager
from strategies.orb_strategy import ORBStrategy

import yaml

cfg = yaml.safe_load(open("config/settings.yaml"))

broker = FyersBroker("CLIENT_ID", "TOKEN")

risk = RiskManager(cfg["capital"], cfg["risk"]["risk_per_trade_pct"])

pm = PortfolioManager(broker, risk)

downloader = HistoricalDownloader("CLIENT_ID", "TOKEN")

strategy = ORBStrategy()


def daily_run():

    symbol = "NSE:NIFTYBANK-INDEX"

    df = downloader.fetch(symbol, timeframe="5")

    sig, sl = strategy.signal(df)

    if sig:
        pm.execute(symbol, sig, df.close.iloc[-1], sl)

import schedule
import time

def job():
    daily_run()

schedule.every(5).minutes.do(job)

print("Engine started... Monitoring market every 5 minutes")

import datetime

while True:
    print("Checking signals at:", datetime.datetime.now())
    schedule.run_pending()
    time.sleep(60)


while True:
    schedule.run_pending()
    time.sleep(1)

