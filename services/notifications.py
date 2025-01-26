import requests
import time

class Notifications:
    def __init__(self, bot_token, chat_id):
        """
        Initialize the Notifications service.

        Args:
            bot_token (str): Telegram bot token.
            chat_id (str): Telegram chat ID.
        """
        if not bot_token or not chat_id:
            raise ValueError("Both bot_token and chat_id are required.")
        self.bot_token = bot_token
        self.chat_id = chat_id

    def send_message(self, message, retries=3, delay=2):
        """
        Send a message via Telegram with retry logic.

        Args:
            message (str): The message to send.
            retries (int): Number of retry attempts in case of failure.
            delay (int): Delay (in seconds) between retry attempts.
        """
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        payload = {"chat_id": self.chat_id, "text": message}

        for attempt in range(1, retries + 1):
            try:
                response = requests.post(url, json=payload)
                if response.status_code == 200:
                    print(f"Notification sent: {message}")
                    return {"status": "success", "response": response.json()}
                else:
                    print(f"Attempt {attempt}: Failed to send notification. Error: {response.text}")

                # Retry after a delay
                if attempt < retries:
                    time.sleep(delay)
            except Exception as e:
                print(f"Attempt {attempt}: Error sending notification: {e}")

        # If all retries fail
        print("All attempts to send notification failed.")
        return {"status": "failure", "error": "Unable to send message after retries."}
