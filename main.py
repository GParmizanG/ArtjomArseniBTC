import os
import requests
from dotenv import load_dotenv

load_dotenv()

WEBHOOK = os.environ.get("DISCORD_WEBHOOK")

API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur"

def main():
    try:
        print("[INFO] service=btc-bot Cron job started")

        response = requests.get(API_URL, timeout=10)
        data = response.json()

        price = data["bitcoin"]["eur"]
        message = f"BTC: {price} EUR"

        requests.post(WEBHOOK, json={"content": message})

        print(f"[INFO] service=btc-bot Sent to Discord: {message}")

    except Exception as e:
        print(f"[ERROR] service=btc-bot {str(e)}")

if __name__ == "__main__":
    main()