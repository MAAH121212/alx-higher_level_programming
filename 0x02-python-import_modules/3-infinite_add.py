#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    sum = 0
    for i in range(length - 1):
        sum += int(sys.argv[i + 1])
    print(sum)
