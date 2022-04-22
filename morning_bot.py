import time
from sender import Sender
from switcher import Switcher
from tg_chats import TGChats
from morning_determiner import MorningDeterminer
from choices_records import ChoicesRecords


class MorningBot:

    def __init__(self) -> None:
        self.sender = Sender()
        self.tg_chats = TGChats()
        self.fetcher = None

    def process(self, person):
        print(f"MorningBot: getting data for the {person}")
        data = self.fetcher.get_morning_data()
        print("data fetched", data)
        self.sender.send_data(data, person)

    def run(self):

        while True:
            time.sleep(5)
            self.tg_chats.list_updates()
            if MorningDeterminer.ismorning():
                for person_id in ChoicesRecords.choices:
                    type_choice = ChoicesRecords.choices[person_id]
                    self.fetcher = Switcher(type_choice)
                    self.process(person_id)


def main():

    MorningBot().run()


if __name__ == "__main__":
    main()
