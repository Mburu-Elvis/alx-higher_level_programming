#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
last_digit = int(repr(number)[-1])
if last_digit > 5:
    print(f"Last digit of {number: d} is {last_digit: d}")
elif last_digit == 0:
    print(f"Last digit of {number: d} is {last_digit: d}")
elif last_digit < 6 and != 0:
    print(f"Last digit of {number: d} is {last_digit: d}")
