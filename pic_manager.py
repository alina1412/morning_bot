import os
from site_pixabay import Pixabay


class PictureManager:

    def get_morning_data(self) -> dict:
        ans = Pixabay.get_answer()
        if self.isvalid(ans):
            return ans
        else:
            print("path of a pic not valid")
            return {}

    def isvalid(self, data) -> bool:
        if "type_picture_path" in data:
            path = data["type_picture_path"]
            return os.path.isfile(path)
        else:
            print("no path of a pic")
            return False
