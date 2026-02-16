import matplotlib.pyplot as plt
import pandas as pd
import time


class LiveDashboard:

    def run(self):

        while True:

            try:
                df = pd.read_csv("journal/trades.csv")

                pnl = df["pnl"].cumsum()

                plt.clf()
                plt.plot(pnl)
                plt.title("Live Equity Curve")
                plt.pause(2)

            except:
                pass

            time.sleep(5)

    def get_options_data(broker):

        positions = broker.get_positions()

        options = []

        for p in positions:
            if "CE" in p["symbol"] or "PE" in p["symbol"]:
                options.append({
                    "symbol": p["symbol"],
                    "type": "CE" if "CE" in p["symbol"] else "PE",
                    "qty": p["qty"],
                    "pnl": p["pnl"]
                })

        return options
