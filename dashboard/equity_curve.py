import matplotlib.pyplot as plt
import pandas as pd

def plot_equity(csv="journal.csv"):
    df = pd.read_csv(csv)
    df["cum"] = df["pnl"].cumsum()
    df["cum"].plot()
    plt.title("Equity Curve")
    plt.show()
