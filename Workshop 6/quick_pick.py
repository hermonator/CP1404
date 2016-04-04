__author__ = "Jesse Hermon"

import random

numberOfQuickPicks = int(input('How many quick picks? '))

for i in range(numberOfQuickPicks):
    for j in range(6):
        random_number = random.randint(1,45)
        print(' {:2d}'.format(random_number), end='')

    print()
