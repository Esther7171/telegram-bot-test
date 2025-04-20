import os
import requests

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_test_alert():
    message = """
🚨 *TEST ALERT* 
This is a verification message from GitHub Actions.
✅ Bot is working!
"""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=payload)
    print(f"Status: {response.status_code}, Response: {response.json()}")

if __name__ == "__main__":
    print("Starting test...")
    send_test_alert()
