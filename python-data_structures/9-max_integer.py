#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or not my_list:
        return None
    max_Value = my_list[0]
    for num in my_list:
        if num > max_Value:
            max_Value = num
    return max_Value
