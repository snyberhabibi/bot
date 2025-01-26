import requests

class Notifications:
    def __init__(self, bot_token, chat_id):
        """
        Initialize the Notifications service.

        Args:
            bot_token (str): Telegram bot token.
            chat_id (str): Telegram chat ID.
        """
        self.bot_token = bot_token
        self.chat_id = chat_id

    def send_message(self, message):
        """
        Send a message via Telegram.

        Args:
            message (str): The message to send.
        """
        try:
            url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
            payload = {"chat_id": self.chat_id, "text": message}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print(f"Notification sent: {message}")
            else:
                print(f"Failed to send notification. Error: {response.text}")
        except Exception as e:
            print(f"Error sending notification: {e}")
