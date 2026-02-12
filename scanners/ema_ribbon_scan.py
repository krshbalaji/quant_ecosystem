def ema_ribbon(df):
    ema10 = df.close.ewm(span=10).mean()
    ema20 = df.close.ewm(span=20).mean()
    ema50 = df.close.ewm(span=50).mean()

    return ema10.iloc[-1] > ema20.iloc[-1] > ema50.iloc[-1]
