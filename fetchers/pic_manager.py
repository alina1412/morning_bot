import os
from fetchers.site_pixabay import Pixabay


class PictureManager:

    async def get_morning_data(self) -> dict:
        ans = await Pixabay.get_answer()
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
