import json

FILE = "data/profit_state.json"

LOCK_PERCENT = 0.50


def update(equity):

    try:
        state = json.load(open(FILE))
    except:
        state = {"peak": equity, "lock": equity}

    if equity > state["peak"]:

        profit = equity - state["lock"]

        lock_amount = state["lock"] + profit * LOCK_PERCENT

        state["peak"] = equity

        state["lock"] = lock_amount

        json.dump(state, open(FILE, "w"))

    return state["lock"]


def allowed(equity):

    state = json.load(open(FILE))

    return equity > state["lock"]
