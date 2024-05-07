#!/usr/bin/python3
if __name__ == "__main__":  # if the script is executed, not imported
    from add_0 import add  # import add function from add_0 module
    a = 1  # assign 1 to a
    b = 2  # assign 2 to b
    print("{} + {} = {}".format(a, b, add(a, b)))  # print the sum of a and b
