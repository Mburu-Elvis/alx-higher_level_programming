#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = repr(number)
last_digit = n[-1]
last = int(last_digit)
if last > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last))
elif last == 0:
    print("Last digit of {} is {} and is 0".format(number, last))
elif last < 0:
    print("Last digit of {} is {} and is not 0".format(number, -last))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, last))
