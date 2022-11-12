import time

from morning_bot.config import Config


class MorningDeterminer:
    @staticmethod
    def ismorning() -> bool:
        """08:00 - 08:05"""
        if Config.DEBUG:
            return True

        BEGIN_H: int = Config.BEGIN_H
        BEGIN_MIN: int = Config.BEGIN_MIN
        END_M: int = Config.END_M

        cur_time: str = time.strftime("%H:%M")

        if BEGIN_H == int(cur_time[:2]) and BEGIN_MIN <= int(cur_time[3:]) <= END_M:
            return True
        return False
