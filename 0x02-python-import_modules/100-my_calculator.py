#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
import sys

if len(sys.argv) != 4:
    if __name__ == '__main__':
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
    sys.exit(1)

operator = sys.argv[2]

if operator not in ('+', '-', '*', '/'):
    if __name__ == '__main__':
        print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[3])

if operator == '+':
    result = add(a, b)
elif operator == '-':
    result = sub(a, b)
elif operator == '*':
    result = mul(a, b)
elif operator == '/':
    result = div(a, b)

if __name__ == '__main__':
    print("{} {} {} = {}".format(a, operator, b, result))
