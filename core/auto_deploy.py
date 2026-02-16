import subprocess
import os


class AutoDeploy:

    def sync(self):

        try:

            subprocess.call(["git", "pull"])

            print("AutoDeploy: pulled latest brain")

        except:

            pass


    def upload(self):

        try:

            subprocess.call(["git", "add", "."])

            subprocess.call([
                "git",
                "commit",
                "-m",
                "Auto brain update"
            ])

            subprocess.call(["git", "push"])

            print("AutoDeploy: pushed brain")

        except:

            pass
