#!/usr/bin/python3
def safe_print_integer(value):
    exec = True
    try :
        formatted_value = "{:d}".format(value)  # Format the integer value
        print(formatted_value)
    except ValueError:
        exec = False
    return exec
