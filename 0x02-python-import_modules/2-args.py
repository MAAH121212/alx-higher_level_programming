#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    length = len(sys.argv)
    if length == 1:
        print("0 arguments.")
    elif length == 2:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(len(sys.argv) - 1))
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{:d}: {}".format(i, arg))
