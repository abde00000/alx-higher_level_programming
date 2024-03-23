#!/usr/bin/python3
def weight_average(my_list=[]):
    top, bot = 0, 0
    for x, y in my_list:
        top += x * y
        bot += y
    return top / bot
