import os
import shutil
import torch


class CentralBrain:

    def __init__(self):

        self.global_model = "data/global_brain.pt"

        self.local_model = "data/lstm_distributed.pt"

        os.makedirs("data", exist_ok=True)


    def upload(self):

        if os.path.exists(self.local_model):

            shutil.copy(self.local_model, self.global_model)

            print("CentralBrain: uploaded local intelligence")


    def download(self):

        if os.path.exists(self.global_model):

            shutil.copy(self.global_model, self.local_model)

            print("CentralBrain: downloaded global intelligence")


    def aggregate(self):

        if not os.path.exists(self.global_model):
            return

        try:

            global_weights = torch.load(self.global_model)

            local_weights = torch.load(self.local_model)

            merged = {}

            for key in global_weights:

                merged[key] = (
                    global_weights[key] + local_weights[key]
                ) / 2

            torch.save(merged, self.global_model)

            print("CentralBrain: aggregated intelligence")

        except Exception as e:

            print("Aggregation error:", e)
