from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = "8581613607:AAEz07YOX2k4Fdol8GNbAtU2x3wJXFJrWpQ"
CHAT_ID = "-1003290859465"

def send_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

@app.route('/alert', methods=['POST'])
def alert():
    data = request.get_json()

    # Extract fields safely
    event = data.get("Event", "N/A")
    symbol = data.get("Symbol", "N/A")
    timeframe = data.get("Timeframe", "N/A")
    price = data.get("Price", "N/A")
    strategy = data.get("Strategy", "N/A")   # ← FIXED HERE

    # Build Telegram message
    text = (
        f"⚡ *{event} Signal Triggered*\n\n"
        f"📌 *Symbol:* {symbol}\n"
        f"⏱ *Timeframe:* {timeframe}\n"
        f"💰 *Price:* {price}\n"
        f"📒 *Strategy:* {strategy}"
    )

    send_telegram(text)
    return "ok", 200


@app.route("/ping")
def ping():
    return {"status": "alive"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
