#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if type(key) is not str:
        key = str(key)
    a_dictionary[key] = value
