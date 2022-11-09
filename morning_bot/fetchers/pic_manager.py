import os

from morning_bot.fetchers.site_pixabay import Pixabay
from morning_bot.fetchers import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class PictureManager:
    async def get_morning_data(self) -> dict:
        ans = await Pixabay.get_answer()
        if self.isvalid(ans):
            return ans
        else:
            logger.debug("path of a pic not valid")
            return {}

    def isvalid(self, data) -> bool:
        if "type_picture_path" in data:
            path = data["type_picture_path"]
            return os.path.isfile(path)
        else:
            logger.debug("no path of a pic")
            return False
