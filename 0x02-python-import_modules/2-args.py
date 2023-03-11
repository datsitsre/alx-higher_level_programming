#!/usr/bin/python3
import sys

if len(sys.argv) - 1 == 0:
    print("{} arguments.".format(0))
else:
    print("{} arguments:".format(len(sys.argv) - 1))
    n = 1
    while (n <= len(sys.argv) - 1):
        print("{}: {}".format(n, sys.argv[n]))
        n += 1
