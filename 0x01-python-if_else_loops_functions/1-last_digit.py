#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    the_number = number * -1
else:
    the_number = number
last_digit = the_number % 10
if number < 0:
    the_last_digit = last_digit * -1
else:
    the_last_digit = last_digit
if the_last_digit > 5:
    print(f"Last digit of {number:d} is {last_digit:d} and is greater than 5")
elif the_last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number:d} is {last_digit:d} \
and is less than 6 and not 0")
elif the_last_digit == 0:
    print(f"Last digit of {number:d} is {last_digit:d} and is 0")
