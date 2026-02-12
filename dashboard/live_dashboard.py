import matplotlib.pyplot as plt
import pandas as pd
import time


def run():

    while True:

        try:
            df = pd.read_csv("journal/trades.csv")

            plt.clf()

            plt.plot(df["capital"])

            plt.title("Equity Curve")

            plt.pause(1)

        except:
            pass

        time.sleep(5)


if __name__ == "__main__":
    run()
