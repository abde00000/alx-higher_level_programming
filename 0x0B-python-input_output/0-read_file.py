#!/usr/bin/python3
"""the module is about the read_file function."""


def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout."""

    with open('UTF8', 'r') as file:
        file_content = file.read()

    print(file_content)
