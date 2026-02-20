import time
import pandas as pd
import yfinance as yf

from core.strategy_loader import load_strategies
from core.paper_broker import PaperBroker
from core.state_engine import state_engine
from infra.telegram_service import send_message


class ExecutionEngine:

    def __init__(self):
        self.strategies = load_strategies()
        self.broker = PaperBroker()

    def fetch_data(self):
        data = yf.download("NIFTYBEES.NS", period="1d", interval="5m")
        
        import pandas as pd

        if isinstance(data.columns, pd.MultiIndex):
            data.columns = [col[0].lower() for col in data.columns]
        else:
            data.columns = [str(col).lower() for col in data.columns]
        return data

    def run(self):
        while True:
            try:
                if not state_engine.state["autonomous"]:
                    time.sleep(5)
                    continue

                data = self.fetch_data()

                for strategy in self.strategies:
                    signal = strategy.generate_signal(data)

                    if signal:
                        price = data["close"].iloc[-1]
                        result = self.broker.execute(signal, price)

                        if result:
                            print(result)
                            send_message(result)

                time.sleep(60)

            except Exception as e:
                print("Execution error:", e)
                time.sleep(10)