#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    skipped = 0
    while count < x:
        try:
            print("{:d}".format(my_list[count]), end="")
            count += 1
        except (ValueError, TypeError):
            count += 1
            skipped += 1

    print()
    return count - skipped
