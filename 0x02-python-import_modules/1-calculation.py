#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a, b = 10, 5
    print("{} + {} = {}".format(a, b, str(add(a, b))))
    print("{} - {} = {}".format(a, b, str(sub(a, b))))
    print("{} * {} = {}".format(a, b, str(mul(a, b))))
    print("{} / {} = {}".format(a, b, str(div(a, b))))
