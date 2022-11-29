#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    sign = -1
    number1 = number * -1
else:
    sign = 1
    number1 = number
last_digit = (number1 % 10) * sign
print(f"Last digit of {number} is {last_digit}", end=" ")
if last_digit > 5:
    print("and is greater than 5")
if last_digit == 0:
    print("and is 0")
if last_digit < 6 and last_digit != 0:
    print("and is less than 6 and not 0")
