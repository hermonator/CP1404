__author_ = 'Jesse Hermon'

import random

def format_currency(value):
    displayed_price = "${:,.2f}".format(price)
    return displayed_price

MAX_INCREASE = 0.175 # 17.5%
MAX_DECREASE = 0.05 # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITAL_PRICE = 10.0
day = 0

price = INITAL_PRICE
displayed_price = format_currency(price)
print('Starting price:','{}'.format(displayed_price))

while price >= MIN_PRICE and price <= MAX_PRICE:
    priceChange = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        priceChange = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_INCREASE and 0
        priceChange = random.uniform(-MAX_DECREASE, 0)

    day = day + 1
    price *= (1 + priceChange)
    displayed_price = format_currency(price)
    print('On day {} price is:'.format(day),"{}".format(displayed_price))
    #print(displayed_price)