import torch
import torch.nn as nn
import numpy as np
import os


class LSTMModel(nn.Module):

    def __init__(self, input_size=1, hidden_size=32):

        super().__init__()

        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)

        self.fc = nn.Linear(hidden_size, 1)


    def forward(self, x):

        out, _ = self.lstm(x)

        out = self.fc(out[:, -1, :])

        return out


class LSTMGPU:

    def __init__(self):

        self.device = torch.device(

            "cuda" if torch.cuda.is_available() else "cpu"
        )

        print("LSTM running on:", self.device)

        self.model = LSTMModel().to(self.device)

        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=0.001)

        self.loss_fn = nn.MSELoss()

        self.file = "data/lstm_gpu.pt"

        if os.path.exists(self.file):

            self.model.load_state_dict(torch.load(self.file))


    def predict(self, prices):

        if len(prices) < 10:

            return 0

        seq = torch.FloatTensor(prices[-10:]).view(1, 10, 1).to(self.device)

        with torch.no_grad():

            pred = self.model(seq).item()

        return 1 if pred > prices[-1] else -1


    def train(self, prices):

        if len(prices) < 11:

            return

        x = torch.FloatTensor(prices[-11:-1]).view(1, 10, 1).to(self.device)

        y = torch.FloatTensor([prices[-1]]).to(self.device)

        pred = self.model(x)

        loss = self.loss_fn(pred, y)

        self.optimizer.zero_grad()

        loss.backward()

        self.optimizer.step()

        torch.save(self.model.state_dict(), self.file)
