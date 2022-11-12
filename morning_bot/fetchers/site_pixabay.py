import os
from random import randint

import aiofiles
import httpx

from ..config import Config


class Pixabay:
    _KEY_PIC = Config.PIC_KEY
    _amount = 200

    @staticmethod
    async def get_answer() -> dict:
        data = await Pixabay.get_data()
        path = await Pixabay.save_data(data)
        return Pixabay.return_data(path)

    @staticmethod
    async def get_data():
        url = "https://pixabay.com/api/"
        params = {
            "key": Pixabay._KEY_PIC,
            "q": "morning",
            "safesearch": "true",
            "per_page": Pixabay._amount,
        }
        async with httpx.AsyncClient() as client:
            resp = await client.get(url, params=params)
            data = resp.json()

            if data and data["totalHits"]:
                return data
            print("No data")
            return None

    @staticmethod
    async def save_data(data):
        rand_choice = randint(0, Pixabay._amount - 1)
        pic_addr = data.get("hits", {}).get(rand_choice, {}).get("webformatURL", None)
        if pic_addr is None:
            return
        randname = Randomizer.randomize_name() + ".jpg"
        folder_name = Config.TMP_DIR
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        dest_with_name = os.path.join(folder_name, randname)
        async with httpx.AsyncClient() as client:
            resp = await client.get(pic_addr)

        async with aiofiles.open(dest_with_name, "wb") as output:
            async for chunk in resp.aiter_bytes():
                if chunk:
                    await output.write(chunk)

        return dest_with_name

    @staticmethod
    def return_data(dest_with_name):
        return {
            "type_picture_path": dest_with_name,
            "default_caption": "from https://pixabay.com/",
        }


class Randomizer:
    @staticmethod
    def randomize_name():
        NAME_LEN = 8
        name = [chr(randint(97, 122)) for _ in range(NAME_LEN)]
        return "".join(name)
