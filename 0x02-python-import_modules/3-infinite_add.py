#!/usr/bin/python3
if __name__== "__main__":
    import sys
    def add(args):
        result = 0
        for i in args:
            result += int(i)
        return result

    print(add(sys.argv[1:]))
