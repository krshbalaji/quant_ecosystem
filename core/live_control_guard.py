import json
import os
from datetime import datetime, timedelta

FILE = "data/live_approval.json"


def init():

    os.makedirs("data", exist_ok=True)

    if not os.path.exists(FILE):

        json.dump({
            "approved": False,
            "timestamp": None
        }, open(FILE, "w"))


def request():

    data = {
        "approved": False,
        "timestamp": str(datetime.now())
    }

    json.dump(data, open(FILE, "w"))


def approve():

    data = {
        "approved": True,
        "timestamp": str(datetime.now())
    }

    json.dump(data, open(FILE, "w"))


def allowed():

    data = json.load(open(FILE))

    if not data["approved"]:
        return False

    ts = datetime.fromisoformat(data["timestamp"])

    return datetime.now() - ts < timedelta(hours=8)
