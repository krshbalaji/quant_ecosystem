# =========================================
# ATM Strike Selector
# =========================================

class StrikeSelector:

    @staticmethod
    def get_atm(price, symbol):

        if "BANKNIFTY" in symbol:
            step = 100
        else:
            step = 50

        return round(price / step) * step
