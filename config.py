import json
import os


class Config:
    BOT_TOKEN = os.environ.get("bot_token")
    print("token", BOT_TOKEN)
    WEATHER_ID = os.environ.get("weather_id")
    PIC_KEY = os.environ.get("pic_key")

    TMP_DIR = "tmp"

    OPTS_KEYBOARD = json.dumps({
        "inline_keyboard": [
            [
                {
                "text": "picture",
                "callback_data": "picture"
                },
                {
                "text": "weather in Moscow",
                "callback_data": "weather"
                }
            ]
        ],   
        "remove_keyboard": True
    })

    # OPTS_KEYBOARD = json.dumps({ 
    #     "keyboard": 
    #     [["Yes"], ["No"]],
    #     # [["Yes", "No"], ["Maybe"], ["1", "2", "3"]], 
    #     # "resize_keyboard": True,
    #     # "one_time_keyboard":True
    #     "remove_keyboard": True
    #     })
