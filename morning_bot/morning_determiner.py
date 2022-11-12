import time

from morning_bot.config import Config


class MorningDeterminer:
    @staticmethod
    def ismorning() -> bool:
        """08:00 - 08:05"""
        if Config.DEBUG:
            return True

        cur_time: str = time.strftime("%H:%M")

        if (
            Config.BEGIN_H == int(cur_time[:2])
            and Config.BEGIN_MIN <= int(cur_time[3:]) <= Config.END_M
        ):
            return True
        return False
