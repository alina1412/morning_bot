import os
from random import randint
import requests
from config import Config


class Pixabay:
    _KEY_PIC = Config.PIC_KEY
    _amount = 200

    @staticmethod
    def get_answer() -> dict:
        data = Pixabay.get_data()
        path = Pixabay.save_data(data)
        return Pixabay.return_data(path)

    @staticmethod
    def get_data():
        url = 'https://pixabay.com/api/'
        params = {"key": Pixabay._KEY_PIC, "q": "morning",
                  "safesearch": "true", "per_page": Pixabay._amount}
        data = requests.get(url, params=params).json()

        if data and data["totalHits"]:
            return data
        else:
            print("No data")
            return None

    @staticmethod
    def save_data(data):
        rand_choice = randint(0, Pixabay._amount - 1)
        # print(len(data["hits"]), data["totalHits"])
        pic_addr = data["hits"][rand_choice]["webformatURL"]
        randname = Randomizer.randomize_name() + ".jpg"
        dest_with_name = os.path.join(Config.TMP_DIR, randname)

        with open(dest_with_name, 'wb') as output:
            for chunk in requests.get(pic_addr):
                output.write(chunk)
        return dest_with_name

    @staticmethod
    def return_data(dest_with_name):
        return {"type_picture_path": dest_with_name,
                "default_caption": "from https://pixabay.com/"}
        # "folder/1.jpeg"


class Randomizer:

    @staticmethod
    def randomize_name():
        NAME_LEN = 8
        name = [chr(randint(97, 122)) for _ in range(NAME_LEN)]
        return "".join(name)

    # def randomize_pic_choice(num):

# print(Pixabay.get_answer())
# print(Randomizer.randomize_name())
