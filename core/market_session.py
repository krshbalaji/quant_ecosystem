from datetime import datetime, time as dtime


PREMARKET_START = dtime(9, 0)
MARKET_OPEN = dtime(9, 15)
MARKET_CLOSE = dtime(15, 30)


class MarketSession:

    def __init__(self):

        print("Market Session Controller initialized")


    def get_phase(self):

        now = datetime.now().time()

        if PREMARKET_START <= now < MARKET_OPEN:
            return "PREMARKET"

        elif MARKET_OPEN <= now <= MARKET_CLOSE:
            return "OPEN"

        else:
            return "CLOSED"
