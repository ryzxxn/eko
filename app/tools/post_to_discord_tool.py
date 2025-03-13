import requests #type: ignore
import json

def send_to_discord(*, webhook_url: str, message: str):
    """
    Send a message to a Discord channel using a webhook URL.

    Parameters:
    - webhook_url: str : The Discord webhook URL.
    - message: str : The message content to send.

    Returns:
    - bool : True if the message was sent successfully, False otherwise.
    """
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'content': message
    }

    response = requests.post(webhook_url, headers=headers, data=json.dumps(data))

    if response.status_code == 204:
        print("Message sent successfully.")
        return True
    else:
        print(f"Failed to send message. Status code: {response.status_code}, Response: {response.text}")
        return False