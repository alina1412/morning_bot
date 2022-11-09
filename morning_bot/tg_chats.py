import time

import httpx

from .config import Config


class TGChats:
    def __init__(self) -> None:
        self.BOT_TOKEN = Config().BOT_TOKEN
        self.offset = 0

    async def list_updates(self, choices_collector):
        print("do func list_updates", time.strftime("%X"))
        response = await self.make_url_request()
        if response:
            command_data = self.parse_response(response)
            if command_data["command"] == "/start":
                await self.greeting_keyboard(command_data)
            elif command_data["command"] == "upd_choice":
                await self.upd_choice(command_data, choices_collector)

    async def make_url_request(self):
        url = f"https://api.telegram.org/bot{self.BOT_TOKEN}/getUpdates"
        params = {"offset": self.offset}  # "timeout": 15

        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response_json = response.json()
            if not response_json["ok"]:
                return
            return response_json["result"]

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
                return {
                    "command": "upd_choice",
                    "chat_id": chat_id,
                    "choice": info_dict["data"],
                }
        return None

    async def upd_choice(self, data, choices_collector):
        choices_collector.save_choice(data["chat_id"], data["choice"])
        text = f"We'll send you a {data['choice']}" + " at the morning!"
        params = {"chat_id": data["chat_id"], "text": text}
        await self.send_tg_message(params)

    async def greeting_keyboard(self, data):
        print("greeting_keyboard")
        params = {
            "chat_id": data["chat_id"],
            "text": "Choose what to get at the morning",
            "reply_markup": Config.OPTS_KEYBOARD,
        }
        await self.send_tg_message(params)
        # time.sleep(2)

    async def send_tg_message(self, params):
        url = f"https://api.telegram.org/bot{self.BOT_TOKEN}/sendMessage"
        async with httpx.AsyncClient() as client:
            await client.post(url, params=params)
