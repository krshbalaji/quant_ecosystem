import json
import os
import shutil


class FederatedEngine:

    def __init__(self):

        self.local = "data/lstm_distributed.pt"

        self.global_model = "data/global_brain.pt"

        os.makedirs("data", exist_ok=True)


    def sync(self):

        if os.path.exists(self.local):

            shutil.copy(self.local, self.global_model)

            print("Federated: uploaded local brain")


    def download(self):

        if os.path.exists(self.global_model):

            shutil.copy(self.global_model, self.local)

            print("Federated: downloaded global brain")


    def merge(self):

        # future weighted merge support
        self.sync()
