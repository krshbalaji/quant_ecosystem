class OptionsMLSelector:

    def select(self, vix, iv):
        if vix > 20:
            return "straddle"
        elif iv_low:
            return "buy_call"
        else:
            return "credit_spread"
