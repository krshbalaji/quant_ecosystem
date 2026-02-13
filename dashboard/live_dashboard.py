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
