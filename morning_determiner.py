import time


class MorningDeterminer:

    @staticmethod
    def ismorning() -> bool:
        # 08:00 - 08:05

        BEGIN_H = 8
        BEGIN_MIN = 0
        END_M = 5

        # TEST_TIME
        # BEGIN_H = 14
        # BEGIN_MIN = 20
        # END_M = 25

        cur_time = time.strftime("%H:%M")

        if (BEGIN_H == int(cur_time[:2]) and
           BEGIN_MIN <= int(cur_time[3:]) <= END_M):
            return True
        return False

# ans = MorningDeterminer.ismorning()
# print(ans)
