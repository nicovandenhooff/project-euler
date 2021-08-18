# Project Euler: Problem 24
# Lexicographic permutations
# Author: Nico Van den Hooff
# Github: https://github.com/nicovandenhooff/project-euler
# Problem: https://projecteuler.net/problem=24

# Note: A brute-force approach is fast in python with the
#       itertools library.  This script runs in approx.
#       1 second on my laptop.


import itertools


def nth_lex_permutation(n, digits):
    """Determines the n-th lexiographic permutations for k digits
    from 0, 1, ... 9.

    Parameters
    ----------
    n : int
        The n-th permutation to find
    digits : int
        Number of digits for permutation, starts at 0 (inclusive)
        until "digits" (exclusive)

    Returns
    -------
    int
        The n-th permutation for k digits
    """

    perms = []
    result = ""

    # generate list of permutations
    for i in itertools.permutations(range(digits)):
        perms.append(i)

    # join the answer together
    for j in perms[n - 1]:
        result += str(j)

    return int(result)


print(nth_lex_permutation(1000000, 10))
