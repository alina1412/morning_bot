import logging

import httpx

from .config import Config

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class TGChats:
    """sends requests to api.telegram.org*"""
    def __init__(self) -> None:
        self.BOT_TOKEN = Config.BOT_TOKEN
        self.offset = 0

    async def list_updates(self, choices_collector):
        # logger.debug("do func list_updates %s", time.strftime("%X"))
        response = await self.make_url_request()
        if not response:
            return
        command_data = self.parse_response(response)
        if not command_data:
            return
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
            return response_json.get("result", False)

    def parse_response(self, updates):
        for upd in updates:
            self.offset = upd["update_id"] + 1

            if "message" in upd:
                chat_id = upd.get("message", {}).get("from", {}).get("id", None)
                if chat_id is None:
                    return None

                user_ask = upd.get("message", {}).get("text", "")
                if user_ask == "/start":
                    return {"command": "/start", "chat_id": chat_id}

            if "callback_query" in upd:
                info_dict = upd["callback_query"]
                chat_id = info_dict.get("from", {}).get("id", None)
                if chat_id is not None:
                    return {
                        "command": "upd_choice",
                        "chat_id": chat_id,
                        "choice": info_dict.get("data", ""),
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

    async def send_tg_message(self, params):
        url = f"https://api.telegram.org/bot{self.BOT_TOKEN}/sendMessage"
        async with httpx.AsyncClient() as client:
            await client.post(url, params=params)
