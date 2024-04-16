#!/usr/bin/python3
"""Defines a function lookup."""


def lookup(obj):
    """Return a list of available attributes and methods of an object."""
    return dir(obj)
