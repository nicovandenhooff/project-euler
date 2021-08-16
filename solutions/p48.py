# Project Euler: Problem 48
# Self powers
# Author: Nico Van den Hooff
# Github: https://github.com/nicovandenhooff/project-euler
# Problem: https://projecteuler.net/problem=48

DIGITS = 10


def self_powers_sum(start, stop):
    """Calculates the sum of a series of self powers.

    Parameters
    ----------
    start : int
        The first number in the series.
    stop : int
        The last number in the series.

    Returns
    -------
    total : int
        The sum of the series of self powers.
    """

    total = 0

    # calculate total
    for i in range(start, stop):
        total += i ** i

    return total


def last_digits(n, length):
    """Returns the last k digits of a number.

    Parameters
    ----------
    n : int
        The number.
    length : int
        The last k number of digits. Must be <= n

    Returns
    -------

        [description]
    """
    digits = str(total)[-length:]
    return digits


total = self_powers_sum(1, 1001)
digits = last_digits(total, DIGITS)
print(digits)
