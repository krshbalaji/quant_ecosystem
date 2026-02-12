def run_trade(strategy, broker, risk, df, symbol):

    sig, level = strategy.signal(df)

    if not sig:
        return

    entry = df.close.iloc[-1]
    qty = risk.calc_qty(entry, level)

    if sig == "BUY":
        broker.place_market(symbol, qty, 1)
    else:
        broker.place_market(symbol, qty, -1)
