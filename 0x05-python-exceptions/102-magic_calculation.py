#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("TOO Far")
            else:
                result = result + ((a ** b) / i)
        except Exception:
            result = b + a

    return result
