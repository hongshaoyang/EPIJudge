from test_framework import generic_test
from test_framework.test_failure import TestFailure
import string

# 6.1, interconvert strings and integers
# SOLUTION
    # build up each digit one by one
    # use chr() and ord() to convert from int to string
    # use string.digits to convert from string to int

def int_to_string(x):
    if x == 0:
        return "0"
    
    is_negative, x = (True, -x) if x < 0 else (False, x)
    lst = []
    while x:
        # use chr and ord 
        lst.insert(0, chr(ord("0") + x%10))
        x //= 10
    
    # append negative sign if needed
    if is_negative:
        lst.insert(0, "-")
    return "".join(lst) 


def string_to_int(s):
    # use string.digits.index(c)
    res, pwr = 0, 0
    for i in range(len(s))[::-1]:
        if i==0 and s[i]=="-":
            return -res
        res += string.digits.index(s[i]) * 10 ** pwr
        pwr += 1
    return res


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
