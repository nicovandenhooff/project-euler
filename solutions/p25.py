# Project Euler: Problem 25
# 1000 digit Fibonacci sequence
# Author: Nico Van den Hooff
# Github: https://github.com/nicovandenhooff/project-euler
# Problem: https://projecteuler.net/problem=25

# Note: This code reuses the fibonacci function from my solution
#       to problem 2 in p02.py.

import math


DIGITS = 1000


def fibonacci(n1, n2):
    """Simple value to calculate the next two values in a fibonacci sequence.

    Parameters
    ----------
    n1 : int
        The first previous value in the sequence.
    n2 : int
        The second previous value in the sequence.

    Returns
    -------
    (n1, n2) : (int, int)
        The next two values in the fibonacci sequence
    """
    temp = n2
    n2 += n1
    n1 = temp

    return n1, n2


def num_digits(n, b=10):
    """Determines the number of digits a number has in base b.

    Parameters
    ----------
    n : int
        The number to determine the number of digits for.
    b : int, optional
        The base to calculate in, by default 10.

    Returns
    -------
    int
        The number of digits the number contains.
    """
    return math.floor(math.log(n, b) + 1)


def big_fibonacci(digits, n1_start=0, n2_start=1):
    """Determines the first fibonacci number with n digits.

    Parameters
    ----------
    digits : int
        The number of digits to search for.
    n1_start : int, optional
        The first value in the fibonacci sequence, by default 0.
    n2_start : int, optional
        The second value in the fibonacci sequence, by default 1.

    Returns
    -------
    n2, count
        The first number with n digits, the index of this number.
    """

    # trivial case
    if digits == 1:
        return 0, 0

    # next values in the sequence
    n1, n2 = fibonacci(n1_start, n2_start)

    # initial count is two since we start with two digits
    count = 2

    # search for the first fibonacci number with n digits
    while num_digits(n2) != digits:
        n1, n2 = fibonacci(n1, n2)
        count += 1

    return n2, count


ans, count = big_fibonacci(DIGITS)
print(count)
