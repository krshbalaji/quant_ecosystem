AUTHORIZED_CHAT_ID = "YOUR_CHAT_ID"


def verify_access(chat_id):

    if str(chat_id) != AUTHORIZED_CHAT_ID:

        print("Unauthorized access blocked")

        return False

    return True
