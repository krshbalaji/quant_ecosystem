import pandas as pd
from fyers_apiv3 import fyersModel
import datetime as dt


class HistoricalDownloader:

    def __init__(self, client_id, token):
        self.fyers = fyersModel.FyersModel(client_id=client_id, token=token)

    def fetch(self, symbol, timeframe="5", days=60):

        end = dt.datetime.now()
        start = end - dt.timedelta(days=days)

        data = {
            "symbol": symbol,
            "resolution": timeframe,
            "date_format": "1",
            "range_from": start.strftime("%Y-%m-%d"),
            "range_to": end.strftime("%Y-%m-%d"),
            "cont_flag": "1"
        }

        res = self.fyers.history(data)

        df = pd.DataFrame(res["candles"],
                          columns=["ts","open","high","low","close","volume"])

        df["time"] = pd.to_datetime(df["ts"], unit="s")
        df.set_index("time", inplace=True)

        return df
