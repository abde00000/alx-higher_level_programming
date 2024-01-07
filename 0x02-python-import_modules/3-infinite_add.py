#!/usr/bin/python3
if __name__ == "__main__":
    result = 0
    import sys
    count = len(sys.argv)
    for n in range(1, count):
        result += int(sys.argv[n])
    print(result)
