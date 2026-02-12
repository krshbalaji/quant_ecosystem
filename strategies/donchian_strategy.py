class Donchian:

    def signal(self, df):

        hi = df.high.rolling(20).max().iloc[-2]
        lo = df.low.rolling(20).min().iloc[-2]

        if df.close.iloc[-1] > hi:
            return "BUY", lo

        if df.close.iloc[-1] < lo:
            return "SELL", hi

        return None, None
