#!/usr/bin/python3
def safe_print_integer(value):
    try:
        formatted_value = "{:d}".format(value)  # Format the integer value
        print(formatted_value)  # Print the formatted value
        return True  # Return True if printing succeeds
    except ValueError:
        return False  # Return False if a ValueError occurs during formatting or printing

