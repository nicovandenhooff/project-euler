# Project Euler: Problem 3
# Largest prime factor
# Author: Nico Van den Hooff
# Github: https://github.com/nicovandenhooff/project-euler
# Problem: https://projecteuler.net/problem=3


import math

TO_FACTOR = 600851475143


def is_prime(num):
    """Determines if a number is prime.

    Parameters
    ----------
    num : int
        The number in question.

    Returns
    -------
    bool
        True if prime, False otherwise.
    """

    # exceptional cases
    if num <= 1:
        return False
    elif num == 2:
        return True

    # limit for divisions
    square_root = int(math.sqrt(num))

    # attempt to find divisor from 2 to square root
    for i in range(2, square_root):
        if num % i == 0:
            return False

    return True


def largest_prime_factor(num):
    """Finds the largest prime factor of a number n.

    Parameters
    ----------
    num : int
        The number to factor.

    Returns
    -------
    factor : int
        The largest prime factor
    """

    factor = 1
    square_root = int(math.sqrt(num) - 1)

    for i in range(square_root):
        if is_prime(i):
            if num % i == 0:
                factor = i

    return factor


print(largest_prime_factor(TO_FACTOR))
