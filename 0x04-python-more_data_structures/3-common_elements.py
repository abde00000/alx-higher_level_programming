#!/usr/bin/python3
def common_elements(set_1=None, set_2=None):
    if set_1 is None or set_2 is None:
        return None
    if not isinstance(set_1, set) or not isinstance(set_2, set):
        return None
    return set_1.intersection(set_2)