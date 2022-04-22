import os
from site_pixabay import Pixabay


class PictureManager:

    def get_morning_data(self) -> dict:
        ans = Pixabay.get_answer()
        if "type_picture_path" in ans:
            path = ans["type_picture_path"]
            if self.isvalid(path):
                return ans
            else:
                print("path of a pic not valid")
                return None
        else:
            print("no path of a pic")
            return None

    def isvalid(self, path):
        return os.path.isfile(path)
    