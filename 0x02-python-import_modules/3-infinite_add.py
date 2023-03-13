#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    answer = 0
    n = len(sys.argv) - 1
    for i in range(n):
        answer += int(sys.argv[i + 1])
    print("{}".format(answer))
