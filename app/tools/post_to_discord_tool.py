import requests #type:ignore
import json

def send_to_discord(*, webhook_url: str = None, message: str):
    """
    Send a message to a Discord channel using a webhook URL.

    Parameters:
    - webhook_url: str : The Discord webhook URL. Defaults to a predefined URL if not provided.
    - message: str : The message content to send.

    Returns:
    - bool : True if the message was sent successfully, False otherwise.
    """
    if webhook_url is None:
        webhook_url = "https://discord.com/api/webhooks/1151473677364379658/a1fsyU8zTLeS_GlcrQ46F2GVIeeGH3Mbw1GBKIpKkFWaPHFipm3sSQz-Da5QNR9NfqvN"

    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'content': message
    }

    try:
        response = requests.post(webhook_url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raise an error for bad status codes
        if response.status_code == 204:
            print("Message sent successfully.")
            return True
    except requests.exceptions.RequestException as e:
        print(f"Failed to send message: {e}")
        return False
