class OptionsORB:

    def signal(self, df):

        first = df.iloc[:3]

        hi = first.high.max()
        lo = first.low.min()

        last = df.iloc[-1]

        if last.close > hi:
            return "CALL", hi

        if last.close < lo:
            return "PUT", lo

        return None, None
