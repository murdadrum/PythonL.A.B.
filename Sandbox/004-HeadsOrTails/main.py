# https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

import random

coin_toss = random.randint(0, 1)
# print(random_integer)

if coin_toss == 0:
    print("Tails")
else:
    print("Heads")
