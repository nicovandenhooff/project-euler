# Project Euler: Problem 7
# 10001st prime
# Author: Nico Van den Hooff
# Github: https://github.com/nicovandenhooff/project-euler
# Problem: https://projecteuler.net/problem=7

# Note: The solution is a bit brute force, albeit an extremely
#       fast vectorized implementation with NumPy.  First, a
#       sieve of Eratosthenes is created in NumPy.  Then, the
#       sieve is used to find all primes between 0 - 100 billion
#       and extracts the 10,001st prime.  I calc'd primes to
#       100 billion to see how fast the script would run on my
#       laptop - which on average took ~8 seconds.

import numpy as np


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


primes = numpy_sieve(1000000000)
print(primes[10000])
