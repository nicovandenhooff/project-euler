# Project Euler: Problem 53
# Combinatoric selections
# Author: Nico Van den Hooff
# Github: https://github.com/nicovandenhooff/project-euler
# Problem: https://projecteuler.net/problem=53

from math import comb

START = 1
STOP = 100
THRESHOLD = 1000000


def combinatoric_selections(start, stop, threshold):
    """Determines the number of combination values > than a threshold.

    Parameters
    ----------
    start : int
        The first value of "n" to start at.
    stop : int
        The last value of "n" to stop at.
    threshold : int
        The threshold to compare each value to.

    Returns
    -------
    total : int
        The number of combinations that evaluate to be > that the threshold.
    """

    total = 0

    for n in range(start, stop + 1):
        for r in range(1, n):
            if comb(n, r) > threshold:
                total += 1

    return total


print(combinatoric_selections(START, STOP, THRESHOLD))
