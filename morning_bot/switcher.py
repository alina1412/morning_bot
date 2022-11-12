from morning_bot.fetchers.pic_manager import PictureManager
from morning_bot.fetchers.temperature_manager import TemperatureManager


class Switcher:
    """returns an instanse of TemperatureManager or PictureManager"""
    def __new__(self, type_choice):
        if type_choice == "picture":
            return PictureManager()
        elif type_choice == "weather":
            return TemperatureManager()
