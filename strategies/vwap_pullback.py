class VWAPPullback:

    def signal(self, df):

        vwap = (df.close * df.volume).cumsum() / df.volume.cumsum()

        last = df.iloc[-1]

        if last.close > vwap.iloc[-1]:
            return "BUY", vwap.iloc[-1]

        if last.close < vwap.iloc[-1]:
            return "SELL", vwap.iloc[-1]

        return None, None
