#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(int(value)))  # Convert to integer and print
        return True
    except (ValueError, TypeError):
        return False
