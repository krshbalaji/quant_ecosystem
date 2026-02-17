"""
ORB Strategy — Autonomous Engine Compatible Version
Opening Range Breakout Strategy
Fully robust for FYERS, Backtesting, Paper Trading, and Live Execution
"""

class ORBStrategy:

    name = "ORBStrategy"

    def __init__(self, opening_candles=3):
        """
        opening_candles = number of candles to define opening range
        Example:
        3 candles on 5min chart = 15min ORB
        """
        self.opening_candles = opening_candles


    def _get_col(self, df, colname):
        """
        Safely fetch column regardless of case
        Supports: high, HIGH, High, etc.
        """
        for c in df.columns:
            if c.lower() == colname.lower():
                return df[c]
        raise Exception(f"Column '{colname}' not found in dataframe. Available: {df.columns}")


    def signal(self, df):
        """
        Returns:
        signal: BUY / SELL / None
        stop_loss: price level or None
        """

        # Safety check
        if df is None or len(df) < self.opening_candles:
            return None, None

        try:
            high_col = self._get_col(df, "high")
            low_col = self._get_col(df, "low")
            close_col = self._get_col(df, "close")

            # Opening range
            opening_range = df.iloc[:self.opening_candles]

            range_high = high_col.iloc[:self.opening_candles].max()
            range_low = low_col.iloc[:self.opening_candles].min()

            # Latest price
            last_close = close_col.iloc[-1]

            # BUY breakout
            if last_close > range_high:
                return "BUY", range_low

            # SELL breakdown
            elif last_close < range_low:
                return "SELL", range_high

            else:
                return None, None

        except Exception as e:

            print(f"ORBStrategy error: {e}")

            return None, None
