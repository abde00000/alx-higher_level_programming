#!/usr/bin/python3
"""the module is about the read_file function."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""

    with open(filename, 'r') as file:
        file_content = file.read()

    print(file_content)
