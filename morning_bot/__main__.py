import asyncio
import logging
import time

from morning_bot.fetchers.pic_manager import PictureManager
from morning_bot.fetchers.temperature_manager import TemperatureManager


from .choices_records import Collector
from .morning_determiner import MorningDeterminer
from .sender import Sender
from .switcher import Switcher
from .tg_chats import TGChats

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class MorningBot:
    def __init__(self) -> None:
        self.sender = Sender()
        self.tg_chats = TGChats()
        self.collector = Collector()

    async def process(self, person: int, manager: PictureManager | TemperatureManager):
        # logger.debug("MorningBot: getting data for the %s %s", person, time.strftime("%X"))
        data: dict = await manager.get_morning_data()
        # logger.debug("data fetched %s %s", data, time.strftime("%X"))
        await self.sender.send_data(data, person)

    async def run(self):

        while True:
            await self.tg_chats.list_updates(self.collector)
            time.sleep(5)

            if MorningDeterminer.ismorning():
                all_choices = self.collector.get_all_choices()
                que = []
                for person_id, choice in all_choices:
                    que.append(self.process(person_id, Switcher(choice)))
                await asyncio.gather(*que)

                for i in range(60):  # 60 - 5 min
                    await self.tg_chats.list_updates(self.collector)
                    # logger.debug("sleep %s", time.strftime("%X"))
                    time.sleep(5)
                print()


def app():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(MorningBot().run())


if __name__ == "__main__":
    app()
