def liquidate(broker):

    positions = broker.get_positions()

    for symbol in positions:

        qty = positions[symbol]["qty"]

        broker.place_order(symbol, "SELL", qty, 0)

    print("Emergency liquidation executed")
