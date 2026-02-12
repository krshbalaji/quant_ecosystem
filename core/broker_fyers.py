from fyers_apiv3 import fyersModel

class FyersBroker:

    def __init__(self, client_id, token):
        self.fyers = fyersModel.FyersModel(
            client_id=client_id,
            token=token,
            log_path=""
        )

    def place_market(self, symbol, qty, side):

        data = {
            "symbol": symbol,
            "qty": qty,
            "type": 2,
            "side": side,
            "productType": "INTRADAY",
            "validity": "DAY"
        }

        return self.fyers.place_order(data)
