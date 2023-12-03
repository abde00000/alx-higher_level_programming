#!/usr/bin/python3
def uppercase(str):
    upper_str = ''
    for char in str:
        if 97 <= ord(char) <= 122:
            upper_char = ord(char) - 32
            upper_str += chr(upper_char)
        else:
            upper_str += char
    return (upper_str)
