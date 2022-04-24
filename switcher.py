from fetchers.pic_manager import PictureManager
from fetchers.temperature_manager import TemperatureManager


class Switcher:
    def __new__(self, type_choice):
        if type_choice == "picture":
            return PictureManager()
        elif type_choice == "weather":
            return TemperatureManager()
