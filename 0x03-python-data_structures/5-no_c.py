#!/usr/bin/env python3
def no_c(my_string):
    if my_string == "":
        return my_string
    no_c_list = []
    for char in my_string:
        if char != 'c' and char != 'C':
            no_c_list.append(char)
    return ''.join(no_c_list)
