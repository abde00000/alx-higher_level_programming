#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    copy_dictionary = a_dictionary.copy()
    sorted(copy_dictionary)
    for key, value in copy_dictionary.items():
        print("{}: {}".format(key, value))
