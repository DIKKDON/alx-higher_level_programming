#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as ve:
        sys.stderr.write("Exception: {}\n".format(ve))
        return False
    return True
