import time
import asyncio
from sender import Sender
from switcher import Switcher
from tg_chats import TGChats
from morning_determiner import MorningDeterminer
from choices_records import Collector


class MorningBot:

    def __init__(self) -> None:
        self.sender = Sender()
        self.tg_chats = TGChats()
        self.collector = Collector()

    async def process(self, person, manager):
        print(f"MorningBot: getting data for the {person}",
              time.strftime('%X'))
        data = await manager.get_morning_data()
        print("data fetched", data, time.strftime('%X'))
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

                for i in range(60):     # 60 - 5 min
                    await self.tg_chats.list_updates(self.collector)
                    print("sleep", time.strftime('%X'))
                    time.sleep(5)
                print()


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(MorningBot().run())


if __name__ == "__main__":
    main()
