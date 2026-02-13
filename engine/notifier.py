import requests

class TelegramNotifier:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id

    def send(self, msg):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        requests.post(url, data={
            "chat_id": self.chat_id,
            "text": msg
        })
