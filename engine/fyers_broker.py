# engine/fyers_broker.py

from fyers_apiv3 import fyersModel


class FyersBroker:

    def __init__(self, client_id, access_token):
        self.client_id = client_id
        self.access_token = access_token

    def connect(self):
        print("✅ Fyers connected")

    def place_order(self, symbol, side, qty):
        print(f"ORDER → {symbol} {side} {qty}")

    # ---------------------------------
    # Place Order
    # ---------------------------------
    def place_order(self, symbol, side, qty):

        data = {
            "symbol": symbol,
            "qty": qty,
            "type": 2,  # market
            "side": 1 if side == "BUY" else -1,
            "productType": "INTRADAY",
            "limitPrice": 0,
            "stopPrice": 0,
            "validity": "DAY"
        }

        return self.fyers.place_order(data)

    # ---------------------------------
    # Get LTP
    # ---------------------------------
    def get_ltp(self, symbol):
        quote = self.fyers.quotes({"symbols": symbol})
        return quote["d"][0]["v"]["lp"]

    # ---------------------------------
    # Close All
    # ---------------------------------
    def close_all(self):
        # simple safe close (optional)
        pass
    def get_trade_history(self):
        """
        Fetch completed trades from Fyers
        """
        try:
            res = self.fyers.tradebook()

            trades = []
            for t in res.get("tradeBook", []):
                trades.append({
                    "symbol": t["symbol"],
                    "side": t["side"],
                    "qty": t["qty"],
                    "price": t["tradePrice"],
                    "pnl": t.get("realizedProfit", 0)
                })

            return trades

        except Exception as e:
            print("History fetch failed:", e)
            return []
