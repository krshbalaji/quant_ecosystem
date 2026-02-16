import torch
import torch.nn as nn
import os


class DistributedLSTM(nn.Module):

    def __init__(self):

        super().__init__()

        self.lstm = nn.LSTM(1, 64, batch_first=True)

        self.fc = nn.Linear(64, 1)


    def forward(self, x):

        out, _ = self.lstm(x)

        return self.fc(out[:, -1, :])


class LSTMDistributedEngine:

    def __init__(self):

        self.device = torch.device(

            "cuda" if torch.cuda.is_available() else "cpu"
        )

        self.model = DistributedLSTM()

        # Multi-GPU support
        if torch.cuda.device_count() > 1:

            print("Using", torch.cuda.device_count(), "GPUs")

            self.model = nn.DataParallel(self.model)

        self.model.to(self.device)

        self.optimizer = torch.optim.Adam(
            self.model.parameters(),
            lr=0.001
        )

        self.loss_fn = nn.MSELoss()

        self.file = "data/lstm_distributed.pt"

        if os.path.exists(self.file):

            self.model.load_state_dict(
                torch.load(self.file)
            )


    def predict(self, prices):

        if len(prices) < 10:

            return 0

        x = torch.FloatTensor(prices[-10:])\
            .view(1, 10, 1)\
            .to(self.device)

        with torch.no_grad():

            pred = self.model(x).item()

        return pred


    def train(self, prices):

        if len(prices) < 11:

            return

        x = torch.FloatTensor(prices[-11:-1])\
            .view(1, 10, 1)\
            .to(self.device)

        y = torch.FloatTensor([prices[-1]])\
            .to(self.device)

        pred = self.model(x)

        loss = self.loss_fn(pred, y)

        self.optimizer.zero_grad()

        loss.backward()

        self.optimizer.step()

        torch.save(
            self.model.state_dict(),
            self.file
        )
