# Project Euler: Problem 5
# Smallest multiple
# Author: Nico Van den Hooff
# Github: https://github.com/nicovandenhooff/project-euler
# Problem: https://projecteuler.net/problem=5

import math
import pprint


START = 1
STOP = 20


def prime_facorization(num):
    """Computes the prime factorization of a number.

    Parameters
    ----------
    num : int
        The number to compute the prime factorization for.

    Returns
    -------
    factors : list of int
        The prime factors of the number.
    """

    # to store the factors
    factors = []

    square_root = int(math.sqrt(num))

    # add number of twos that evenly divide number to factors
    while num % 2 == 0:
        factors.append(2)
        num = num // 2

    # add odd primes that evenly divide number to factors
    for i in range(3, square_root + 1, 2):
        while num % i == 0:
            factors.append(i)
            num = num // i

    # if there is a number > 2 remaining, add to factors
    # for a prime factorization, there is at most 1 prime
    # factor of n greater than the square root of n
    if num > 2:
        factors.append(num)

    return factors


def get_prime_factorizations(start, stop):
    """Calculates the prime factorizations for a range of values.

    Parameters
    ----------
    start : int
        The start of the range of values (inclusive)
    stop : int
        The end of the range of values (exclusive)

    Returns
    -------
    factorization : dict {int : list of int}
        A dictionary of factorizations for the range of numbers.
        The (key, value) pair is (number, prime factors), where
        the prime factors are held in a list.
    """
    # to hold the factorizations
    factorizations = {}

    # compute prime factorization for each value in range and add to dict
    for i in range(start, stop):
        factorizations[i] = prime_facorization(i)

    return factorizations


def get_smallest_multiple(factorizations):
    """Returns the smallest multiple for a range of numbers.

    To calculate the smallest multiple, the greatest power of each
    prime is found first, and the resulting answer is the multipication
    of the greatest powers.

    In other words, the result is the smallest positive number that is
    evenly divisible by each number in the range.

    Parameters
    ----------
    factorizations : dict {int : list of ints}
        The prime factorizations for the range of numbers.

    Returns
    -------
    result : int
        The smallest multiple.
    """
    result = 1

    # to store the unique prime factors
    unique_factors = []

    # create one list of all factorizations
    for factorization in factorizations.values():
        unique_factors.extend(factorization)

    # extract unique prime factors
    unique_factors = set(unique_factors)

    # to store the greatest power of each unique prime factor
    factors = {k: 0 for k in unique_factors}

    # find the greatest power of each prime within all prime factorizations
    for factorization in factorizations.values():
        for value in factorization:
            if factorization.count(value) > factors[value]:
                factors[value] = factorization.count(value)

    # compute the product of the greatest power for each prime factorization
    for factor, power in factors.items():
        result *= factor ** power

    return factors, result


# prime factorizations
factorizations = get_prime_factorizations(START, STOP)

# each multiple, answer
factors, result = get_smallest_multiple(factorizations)

# print the results
print(
    "The smallest number evenly divisble by the numbers "
    + str(START)
    + " to "
    + str(STOP)
    + " is: "
    + str(result)
)
print("The prime factorization of " + str(result) + " is (factor:power): ")
pprint.pprint(factors)
