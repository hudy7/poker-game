from poker import Poker
from random import randint
import time
import os

if __name__ == "__main__":
    for i in range(100):
        p = Poker(randint(2,9))
        time.sleep(10)
        os.system('clear')
