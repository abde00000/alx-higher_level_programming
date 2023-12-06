#!/usr/bin/python3
import sys
len = len(sys.argv)
if len == 1:
    print(f"{len - 1} argument.")
else:
    print(f"{len - 1} arguments:")
    for n in range(1, len):
        argv = sys.argv[n]
        print("{}: {}".format(n, argv))
