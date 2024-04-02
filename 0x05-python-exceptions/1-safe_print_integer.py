#!/usr/bin/python3
def safe_print_integer(value):
    exec = True
    try :
        print("{:d}".format(value))
    except ValueError:
        exec = False
    return exec
