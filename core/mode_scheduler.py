from datetime import datetime
import json

def update_mode():

    today = datetime.now().strftime("%A")

    if today == "Wednesday":
        mode = "LIVE"
    else:
        mode = "PAPER"

    with open("config/trading_mode.json","w") as f:
        json.dump({"mode": mode}, f)

    print("Trading mode:", mode)
