import pandas as pd


class EMARibbon:
    """
    EMA Ribbon Trend Strategy
    Used by optimizer + engine
    """

    name = "EMA Ribbon"

    def generate_signals(self, df: pd.DataFrame):

        df["ema10"] = df.close.ewm(span=10).mean()
        df["ema20"] = df.close.ewm(span=20).mean()
        df["ema50"] = df.close.ewm(span=50).mean()

        df["long"] = (df["ema10"] > df["ema20"]) & (df["ema20"] > df["ema50"])
        df["short"] = (df["ema10"] < df["ema20"]) & (df["ema20"] < df["ema50"])

        return df
