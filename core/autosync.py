import subprocess
import threading
import time
import os


class AutoSync:
    def __init__(self, interval=600, auto_start=False):
        self.interval = interval
        self.running = False
        self.thread = None
        self.auto_start = auto_start

    def check_git(self):
        if not os.path.exists(".git"):
            print("AutoSync: Not a git repository.")
            return

        print("🔄 AutoSync: Checking for remote updates...")
        try:
            subprocess.run(
                ["git", "pull"],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            print("✅ Git synced successfully.")
        except subprocess.CalledProcessError as e:
            print("⚠ Git sync failed:", e.stderr.decode())

    def start(self):
        if self.running:
            return

        self.running = True

        if self.auto_start:
            self.check_git()

        self.thread = threading.Thread(target=self._loop, daemon=True)
        self.thread.start()

    def stop(self):
        self.running = False

    def _loop(self):
        while self.running:
            time.sleep(self.interval)
            self.check_git()
