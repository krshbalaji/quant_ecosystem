CONTROL_MODE = "AUTO"  # AUTO / MANUAL

def set_manual():
    global CONTROL_MODE
    CONTROL_MODE = "MANUAL"

def set_auto():
    global CONTROL_MODE
    CONTROL_MODE = "AUTO"

def is_auto():
    return CONTROL_MODE == "AUTO"


