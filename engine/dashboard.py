import matplotlib.pyplot as plt


def show_dashboard(stats):

    print("\n========== BACKTEST RESULT ==========")
    print("Trades   :", stats["trades"])
    print("Winrate  :", stats["winrate"], "%")
    print("PnL      :", stats["pnl"])
    print("====================================\n")

    plt.plot(stats["equity_curve"])
    plt.title("Equity Curve")
    plt.xlabel("Trades")
    plt.ylabel("PnL")
    plt.show()
