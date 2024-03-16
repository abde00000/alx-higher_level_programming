#!/usr/bin/env python3
def no_c(my_string):
    if my_string == "":
        return my_string
    no_c = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            pass
        else:
            no_c = no_c + i
    return no_c
