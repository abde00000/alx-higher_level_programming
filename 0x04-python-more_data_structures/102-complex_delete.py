#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    else:
        del_keys = {key for key, val in a_dictionary.items() if val == value}
        for key in del_keys:
            del a_dictionary[key]
        return a_dictionary
