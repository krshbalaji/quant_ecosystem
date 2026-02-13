from journal.trade_journal import TradeJournal


class PortfolioManager:

    def __init__(self, broker, risk):
        self.broker = broker
        self.risk = risk
        self.journal = TradeJournal()

    def execute(self, symbol, side, entry, sl):

        qty = self.risk.calc_qty(entry, sl)

        side_code = 1 if side=="BUY" else -1

        self.broker.place_market(symbol, qty, side_code)

        self.journal.log(symbol, side, qty, entry)
