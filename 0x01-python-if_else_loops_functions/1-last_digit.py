#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = int(repr(number)[-1])
if number < 0:
    num *= -1
if num > 5:
    print(f"Last digit of {number:d} is {number1:d} and is greater than 5")
elif num == 0:
    print(f"Last digit of {number:d} is {number1:d} and is 0")
else:
    print(f"Last digit of {number:d} is {num:d} and is less than 6 and not 0")
