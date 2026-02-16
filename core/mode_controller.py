import json
import datetime


def enforce_mode():

    today = datetime.datetime.now().strftime("%A")

    if today == "Wednesday":

        mode = "LIVE"

    else:

        mode = "PAPER"


    json.dump({"mode": mode}, open("config/trading_mode.json", "w"))

    return mode
