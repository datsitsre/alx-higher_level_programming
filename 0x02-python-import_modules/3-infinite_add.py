#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    answer = 0
    if len(sys.argv) - 1 == 0:
        print("{} arguments.".format(0))
    else:
        n = len(sys.argv) - 1
        for i in range(n):
            answer += int(sys.argv[i + 1])
        print("{}".format(answer))
