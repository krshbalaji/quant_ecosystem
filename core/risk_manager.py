class RiskManager:

    def __init__(self, capital, risk_pct):
        self.capital = capital
        self.risk_pct = risk_pct

    def calc_qty(self, entry, sl):
        risk_amt = self.capital * self.risk_pct / 100
        dist = abs(entry - sl)

        if dist == 0:
            return 0

        return max(1, int(risk_amt / dist))
