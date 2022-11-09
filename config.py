import json

from dotenv import load_dotenv
from os import environ


class Config:
    BOT_TOKEN = environ.get("bot_token")
    print("token", BOT_TOKEN)
    WEATHER_ID = environ.get("weather_id")
    PIC_KEY = environ.get("pic_key")

    BEGIN_H = int(environ.get("BEGIN_H", 8))
    BEGIN_MIN = int(environ.get("BEGIN_MIN", 0))
    END_M = int(environ.get("BEGIN_MIN", 5))

    TMP_DIR = "tmp"

    OPTS_KEYBOARD = json.dumps(
        {
            "inline_keyboard": [
                [
                    {"text": "picture", "callback_data": "picture"},
                    {"text": "weather in Moscow", "callback_data": "weather"},
                ]
            ],
            "remove_keyboard": True,
        }
    )

    # OPTS_KEYBOARD = json.dumps({
    #     "keyboard":
    #     [["Yes"], ["No"]],
    #     # [["Yes", "No"], ["Maybe"], ["1", "2", "3"]],
    #     # "resize_keyboard": True,
    #     # "one_time_keyboard":True
    #     "remove_keyboard": True
    #     })
