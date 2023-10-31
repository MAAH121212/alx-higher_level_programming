#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
string = "Last digit of"
mod = number % 10 if number > 10 else number % -10
if number > 5:
    print(f"{string:s} {number:d} is {mod:d} and is greater than 5")
elif number == 0:
    print(f"{string:s} {number:d} is {mod:d} and is 0")
else:
    print(f"{string:s} {number:d} is {mod:d} and is less than 6 and not 0")
