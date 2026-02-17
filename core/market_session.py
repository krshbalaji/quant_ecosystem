from datetime import datetime, time as dtime


MARKET_OPEN = dtime(9, 15)
MARKET_CLOSE = dtime(15, 30)


class MarketSession:

    def __init__(self):

        print("Market Session Controller initialized")


    def is_market_open(self):

        now = datetime.now().time()

        return MARKET_OPEN <= now <= MARKET_CLOSE


    def get_status(self):

        if self.is_market_open():

            return "OPEN"

        return "CLOSED"
