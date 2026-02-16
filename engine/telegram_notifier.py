# ======================================
# TELEGRAM ALERTS
# ======================================

import requests

class TelegramNotifier:

    def __init__(self,
                 token="8299955382:AAEhg6HGmGq57fKS7PeYcj0KH1nATcdnJBM",
                 chat_id="23687351"):

        self.token = token
        self.chat_id = chat_id
    
    def notify(self, msg):
        self.send_message(msg)

    def send(self, msg):
        try:
            url = f"https://api.telegram.org/bot{self.token}/sendMessage"
            requests.post(url, data={
                "chat_id": self.chat_id,
                "text": msg
            })
        except:
            pass
