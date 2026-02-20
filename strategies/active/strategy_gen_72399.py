
import pandas as pd
import talib

class AssimilatedStrategy:

    name = "AssimilatedStrategy"

    def generate_signal(self, data):

        close = data["close"]

        rsi = talib.RSI(close)

        if rsi.iloc[-1] < 50:
            return "BUY"

        elif rsi.iloc[-1] > 70:
            return "SELL"

        return None
