# Project Euler: Problem 41
# Pandigital prime
# Author: Nico Van den Hooff
# Github: https://github.com/nicovandenhooff/project-euler
# Problem: https://projecteuler.net/problem=41

# Note: I reuse my num_digits function from problem 25 in p25.py
#       as well as my numpy_sieve function from problem 7 in p07.py
#       in this solution.  The logic I apply to solve this problem is:
#           - Create a numpy array of all primes between 0 to 100000000
#           - Apply a custom vectorized numpy function to find the max
#             pan-digital prime in the array
#       The script runs in about 13 seconds, where the majority of the
#       time is spent generating the list of primes.

import numpy as np
import math


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


def numpy_sieve(num):
    """Sieve of Eratosthenes implemented with NumPy.

    Parameters
    ----------
    num : int
        The limit to search for primes until.

    Returns
    -------
    primes : np.array
        NumPy array containing all primes up to n.
    """
    # array of True values for sieve
    primes = np.ones(num, dtype=bool)

    # 0 and 1 are not prime
    primes[0] = primes[1] = False

    # filter out non-prime values
    for i in range(2, int(np.sqrt(num) + 1)):
        if primes[i]:
            primes[i * i :: i] = False

    # extract prime numbers
    primes = np.flatnonzero(primes)

    return primes


def is_pandigital(number):
    """Determines if a number is pandigital.

    Parameters
    ----------
    number : int
        The number in question.

    Returns
    -------
    int
        The number if pandigital, otherwise 0
    """

    # the number of digits the number has
    n = num_digits(number)

    # set of digits in the number
    digits = set([int(i) for i in str(number)])

    # set of digits required for the number to be pandigital
    pan_digits = set(range(1, n + 1))

    # compare number of digits to the number that is required
    if n != len(pan_digits):
        return 0

    # if digits contains everything required, it is pan-digital
    elif pan_digits.issuperset(digits):
        return number
    # catch all
    else:
        return 0


# vectorize function with numpy
vfunc = np.vectorize(is_pandigital)

# generate array of primes
primes = numpy_sieve(100000000)

print(np.max(vfunc(primes)))
