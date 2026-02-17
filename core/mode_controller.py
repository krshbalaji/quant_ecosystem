# core/mode_controller.py

class ModeController:

    def __init__(self):

        self.mode = "PAPER"

        print("Mode Controller initialized in PAPER mode")


    def get_mode(self):

        return self.mode


    def set_mode(self, new_mode):

        new_mode = new_mode.upper()

        if new_mode in ["PAPER", "LIVE", "BACKTEST"]:

            old_mode = self.mode

            self.mode = new_mode

            print(f"Mode switched: {old_mode} → {new_mode}")

            return True

        print("Invalid mode:", new_mode)

        return False


    def is_live(self):

        return self.mode == "LIVE"


    def is_paper(self):

        return self.mode == "PAPER"


    def is_backtest(self):

        return self.mode == "BACKTEST"



# GLOBAL INSTANCE (singleton)
mode_controller = ModeController()



# THIS IS THE FUNCTION YOUR SYSTEM NEEDS
def enforce_mode():

    current = mode_controller.get_mode()

    print(f"Mode enforcement active → {current}")

    return current
