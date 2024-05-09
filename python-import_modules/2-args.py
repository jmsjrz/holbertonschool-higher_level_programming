#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    num_args = len(argv)

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(num_args))

    if num_args != 0:
        for index in range(1, num_args):
            print("{}: {}".format(index, argv[index]))
