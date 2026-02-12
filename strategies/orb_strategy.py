class ORBStrategy:

    def signal(self, df):

        first15 = df.iloc[:3]

        hi = first15.high.max()
        lo = first15.low.min()

        last = df.iloc[-1]

        if last.close > hi:
            return "BUY", hi

        if last.close < lo:
            return "SELL", lo

        return None, None
