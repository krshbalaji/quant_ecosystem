import time


class SystemGuard:

    def __init__(self):

        self.last_check = time.time()


    def alive(self):

        # Always return True unless extended later
        self.last_check = time.time()

        return True


    def heartbeat(self):

        self.last_check = time.time()


    def status(self):

        return {

            "alive": True,
            "last_check": self.last_check
        }
