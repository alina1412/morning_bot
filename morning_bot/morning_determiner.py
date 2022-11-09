import time

from morning_bot.config import Config


class MorningDeterminer:
    @staticmethod
    def ismorning() -> bool:
        # 08:00 - 08:05
        BEGIN_H = Config().BEGIN_H
        BEGIN_MIN = Config().BEGIN_MIN
        END_M = Config().END_M

        cur_time = time.strftime("%H:%M")

        if BEGIN_H == int(cur_time[:2]) and BEGIN_MIN <= int(cur_time[3:]) <= END_M:
            return True
        return False


# ans = MorningDeterminer.ismorning()
# print(ans)
