#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, div, mul, sub
    if len(sys.argv[1:]) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    ops = {"+": add, "-": sub, "/": div, "*": mul}
    operator = sys.argv[2]
    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a, b = int(sys.argv[1]), int(sys.argv[3])
    results = ops[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, results))


