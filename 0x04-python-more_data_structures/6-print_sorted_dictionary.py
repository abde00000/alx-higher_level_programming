#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    copy_dictionary = a_dictionary.copy()
    sor = sorted(copy_dictionary)
    for key in sor:
        print("{}: {}".format(key, copy_dictionary[key]))
