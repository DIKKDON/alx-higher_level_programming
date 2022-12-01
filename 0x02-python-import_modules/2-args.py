#!/usr/bin/python3

from sys import argv

# argument count minus the name of the script
argc = len(argv) - 1
if __name__ == '__main__':
    if argc < 1:
        print("0 arguments.")
    else:
        if argc == 1:
            print(f"{argc} argument:")
        else:
            print(f"{argc} arguments:")
        for index in range(1, argc + 1):
            print(f"{index}: {argv[index]}")
