import json
import os

FILE = "data/pin.json"

DEFAULT_PIN = "2580"


def init():

    if not os.path.exists(FILE):

        json.dump({"pin": DEFAULT_PIN}, open(FILE, "w"))


def verify(pin):

    data = json.load(open(FILE))

    return pin == data["pin"]
