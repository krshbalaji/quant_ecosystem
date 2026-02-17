# core/mode_controller.py

MODE = "PAPER"

print("Mode Controller initialized in PAPER mode")


def set_mode(new_mode):
    global MODE

    new_mode = new_mode.upper()

    if new_mode in ["PAPER", "LIVE", "STOP"]:
        MODE = new_mode
        print(f"Mode switched to {MODE}")
        return True

    print("Invalid mode:", new_mode)
    return False


def get_mode():
    return MODE


def is_live():
    return MODE == "LIVE"


def is_paper():
    return MODE == "PAPER"


def is_stopped():
    return MODE == "STOP"
