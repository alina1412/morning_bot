import time
import requests
from config import Config
from choices_records import ChoicesRecords


class TGChats:

    def __init__(self) -> None:
        self.BOT_TOKEN = Config().BOT_TOKEN
        self.offset = 0

    def list_updates(self):
        print("do func list_updates")
        response = self.make_url_request()
        if response:
            command_data = self.parse_response(response)
            if command_data["command"] == "/start":
                self.greeting_keyboard(command_data)
            elif command_data["command"] == "upd_choice":
                self.upd_choice(command_data)

    def make_url_request(self):
        url = f"https://api.telegram.org/bot{self.BOT_TOKEN}/getUpdates"
        params = {"offset": self.offset, "timeout": 15}
        response = requests.post(url, params)
        response_json = response.json()
        if not response_json['ok']:
            return
        return response_json['result']

    def parse_response(self, updates):
        for upd in updates:
            self.offset = upd["update_id"] + 1

            if "message" in upd:
                chat_id = upd["message"]["from"]["id"]
                if "text" in upd["message"]:
                    user_ask = upd["message"]["text"]
                    if user_ask == "/start":
                        return {"command": "/start", "chat_id": chat_id}
       
            if "callback_query" in upd:
                info_dict = upd["callback_query"]
                chat_id = info_dict["from"]["id"]
                return {"command": "upd_choice", "chat_id": chat_id,
                        "choice": info_dict["data"]}
        return None

    def upd_choice(self, data):
        chat_id = data["chat_id"]
        ChoicesRecords.choices[chat_id] = data["choice"]
        text = (f"We'll send you a {ChoicesRecords.choices[chat_id]}" +
                "at the morning!")
        params = {'chat_id': chat_id, 'text': text}
        self.send_tg_message(params)

    def greeting_keyboard(self, data):
        print("greeting_keyboard")
        params = {'chat_id': data["chat_id"],
                  'text': 'Choose what to get at the morning',
                  'reply_markup': Config.OPTS_KEYBOARD}
        self.send_tg_message(params)
        time.sleep(2)

    def send_tg_message(self, params):
        url = f"https://api.telegram.org/bot{self.BOT_TOKEN}/sendMessage"
        requests.post(url, params=params)
