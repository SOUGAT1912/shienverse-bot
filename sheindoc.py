import requests
import time
import os
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

BOT_TOKEN = os.getenv("8395272102:AAHwDFC9HiUjBUJZsmFN9N_eAULkiNB8bbc")
CHANNEL_ID = os.getenv("1003758543533")

URL = "https://m.shein.com/sheinverse"

bot = Bot(token=BOT_TOKEN)
last_status = None

def check_sheinverse():
    global last_status
    try:
        r = requests.get(URL, timeout=10)
        text = r.text.lower()

        active = "sheinverse" in text or "voucher" in text

        if last_status is None:
            last_status = active
            return

        if active != last_status:
            keyboard = [[
                InlineKeyboardButton(
                    "🧾 Click here to access the SHEINVERSE voucher catalog",
                    url=URL
                )
            ]]

            bot.send_message(
                chat_id=CHANNEL_ID,
                text="🚨 SHEINVERSE UPDATE DETECTED!",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

            last_status = active

    except Exception as e:
        print(e)

while True:
    check_sheinverse()
    time.sleep(60)