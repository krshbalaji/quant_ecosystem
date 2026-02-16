import json
from datetime import datetime, timedelta


class SystemGuard:

    def allow_live(self):

        config = json.load(open("config/system_mode.json"))

        start = datetime.fromisoformat(config["start_date"])

        moratorium = timedelta(weeks=config["moratorium_weeks"])

        if datetime.now() < start + moratorium:

            today = datetime.now().strftime("%A")

            if today != "Wednesday":

                print("Moratorium active: Only PAPER allowed")

                return False

        return True
