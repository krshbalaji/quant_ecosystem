def get_atm_strike(price, step=100):

    return round(price/step)*step


def build_option_symbol(index, strike, side):

    if side == "CALL":
        return f"NSE:{index}{strike}CE"
    else:
        return f"NSE:{index}{strike}PE"
