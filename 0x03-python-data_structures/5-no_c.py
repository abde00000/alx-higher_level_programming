#!/usr/bin/env python3
def no_c(my_string):
    no_c_str = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            no_c_str += char
    return no_c_str
