# Project Euler: Problem 30
# Digit fifth powers
# Author: Nico Van den Hooff
# Github: https://github.com/nicovandenhooff/project-euler
# Problem: https://projecteuler.net/problem=30

# Note: This code reuses the num_digits function from my solution
#       to problem 25 in p25.py.

import math

POWER = 5


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


def upper_limit(power):
    """Calculates the upper limit used in finding digit power sums.

    Assumed to be in base 10.  In base 10, 9 is the highest single
    digit, so the upper limit is calculated as:
           9 ** power * num_digits(9 ** power)

    Parameters
    ----------
    power : int
        The power to find the limit for.

    Returns
    -------
    limit : int
        The upper limit to search until.
    """
    limit = 9 ** power * num_digits(9 ** power)
    return limit


def digit_sum(n, power=1, b=10, factorial=False):
    """Implements the formula to find the sum of the digits in a number.

    Formula: https://en.wikipedia.org/wiki/Digit_sum

    Parameters
    ----------
    n : int
        The number to sum the digits for.
    power : int, optional
        The power to raise each digit to (if relevant), by default 1
    b : int, optional
        The base, by default 10
    factorial : bool, optional
        Whether to perform a factorial on each digit, by default false

    Returns
    -------
    total : int
        The digit sum.
    """
    # number of digits
    k = num_digits(n)

    # digit sum
    total = 0

    for i in range(k):
        # value of each digit
        d_i = ((n % b ** (i + 1)) - (n % b ** i)) // (b ** i)

        # raise to the power if looking for power digit sums
        if power != 1:
            d_i = d_i ** power

        # take a factorial of each digit (used in problem 34)
        if factorial:
            d_i = math.factorial(d_i)

        total += d_i

    return total


def find_numbers(power, upper_limit):
    """Determines the set of numbers that can be written as the sum
    of the desired power of their digits.

    Parameters
    ----------
    power : int
        The power each digit is raised too.
    upper_limit : int
        The upper limit to search until.

    Returns
    -------
    results, total : list of int, int
        The numbers, and sum of the numbers.
    """
    results = []

    # search for valid numbers
    for i in range(2, upper_limit):
        if digit_sum(i, power) == i:
            results.append(i)

    # calculate sum of numbers
    total = sum(results)

    return results, total


limit = upper_limit(POWER)
results, total = find_numbers(POWER, limit)
print(results)
print(total)
