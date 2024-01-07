#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = len(sys.argv)
    if argv == 1:
        print("{} arguments.".format(argv - 1))
    else:
        print("{} arguments:".format(argv - 1))
        for n in range(1, argv):
            print("{}: {}".format(n, sys.argv[n]))
