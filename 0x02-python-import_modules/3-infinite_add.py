#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        results = 0
    else:
        results = 0
        for n in range(1, len(sys.argv)):
            results += int(sys.argv[n])
    print("{}".format(results))
