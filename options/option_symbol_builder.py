# =========================================
# Option symbol formatter for FYERS
# =========================================

import datetime


class OptionBuilder:

    @staticmethod
    def weekly_expiry():

        today = datetime.date.today()
        thursday = today + datetime.timedelta((3 - today.weekday()) % 7)

        return thursday.strftime("%d%b").upper()

    @staticmethod
    def build(symbol, strike, side):

        expiry = OptionBuilder.weekly_expiry()

        typ = "CE" if side == "BUY" else "PE"

        return f"{symbol}{expiry}{strike}{typ}"
