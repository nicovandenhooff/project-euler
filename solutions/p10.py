# Project Euler: Problem 10
# Summation of primes
# Author: Nico Van den Hooff
# Github: https://github.com/nicovandenhooff/project-euler
# Problem: https://projecteuler.net/problem=10

# Note: I reuse my sieve of Eratosthenes built in NumPy from
#       problem 7 at p07.py in this solution.

import numpy as np


LIMIT = 2000000


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


print(np.sum(numpy_sieve(LIMIT)))
