import requests

def send(token, chat, msg):
    url = f"https://api.telegramimport requests


def send(token, chat_id, msg):

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    requests.post(url, data={
        "chat_id": chat_id,
        "text": msg
    })
.org/bot{token}/sendMessage"
    requests.post(url, data={"chat_id": chat, "text": msg})
