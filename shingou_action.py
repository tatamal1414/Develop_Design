from enum import Enum
from logging import raiseExceptions

class Shingou(Enum):
    RED=1
    BLUE=2
    YELLOW=3


def act_shingou(color):
    shingou = Shingou(color)
    if shingou is Shingou.RED:
        print("とまれ")
    elif shingou is Shingou.BLUE:
        print("すすめ")
    elif shingou is Shingou.YELLOW:
        print("ちゅうい")
    else:
        raise Exception("信号機の色に対応していません")

    return

