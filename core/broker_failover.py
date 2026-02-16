from broker.fyers_paper import PaperBroker
from core.fyers_auth import FyersBroker


class BrokerFailover:

    def __init__(self):

        self.primary = None

        self.secondary = PaperBroker()


    def connect(self):

        try:

            self.primary = FyersBroker()

            return self.primary

        except:

            print("LIVE broker failed, switching to PAPER")

            return self.secondary
