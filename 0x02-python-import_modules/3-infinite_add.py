#!/usr/bin/python3
if __name__ == "__main__":
    result = 0
    import sys
    for n in sys.argv[1:]:
        result += int(n)
    print(result)
