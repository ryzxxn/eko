import requests #type:ignore
import json #type:ignore

def send_to_discord(message:str):
    webhook_url = "https://discord.com/api/webhooks/1151473677364379658/a1fsyU8zTLeS_GlcrQ46F2GVIeeGH3Mbw1GBKIpKkFWaPHFipm3sSQz-Da5QNR9NfqvN"
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