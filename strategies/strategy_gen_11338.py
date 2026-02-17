class SwingBBEMA:

    def signal(self, df):

        mid = df.close.rolling(20).mean()
        std = df.close.rolling(20).std()

        upper = mid + 2*std
        lower = mid - 2*std

        ema20 = df.close.ewm(span=20).mean()

        if df.close.iloc[-1] < lower.iloc[-1]:
            return "BUY", lower.iloc[-1]

        if df.close.iloc[-1] < ema20.iloc[-1]:
            return "SELL", upper.iloc[-1]

        return None, None
