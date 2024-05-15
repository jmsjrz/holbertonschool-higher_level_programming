#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Try to format and print the value as an integer
        print("{:d}".format(value))
        # If successful, return True
        return True
    except ValueError:
        # Handle the case where the value cannot be formatted as an integer
        return False
    except TypeError:
        # Handle the case where the type of the value is not suitable for
        #  integer formatting
        return False
