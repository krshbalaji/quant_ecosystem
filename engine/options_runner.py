from core.option_selector import get_atm_strike, build_option_symbol


def run_option_trade(strategy, broker, risk, df, index_name):

    sig, level = strategy.signal(df)

    if not sig:
        return

    price = df.close.iloc[-1]

    strike = get_atm_strike(price)

    symbol = build_option_symbol(index_name, strike, sig)

    qty = 1  # small capital safety

    side = 1 if sig=="CALL" else -1

    broker.place_market(symbol, qty, side)
