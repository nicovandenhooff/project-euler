# Project Euler: Problem 9
# Special Pythagorean triplet
# Author: Nico Van den Hooff
# Github: https://github.com/nicovandenhooff/project-euler
# Problem: https://projecteuler.net/problem=9

LIMIT = 1000


def pythagorean_triplet(p):
    """Calculates and returns a pythagorean triplet a^2 + b^2 = c^2
       such that a < b < c and a + b + c = p.

    Parameters
    ----------
    p : int
        The sum of the terms in the pythagorean triplet.

    Returns
    -------
    a, b, c : tuple of int
        The terms of a pythagorean triplet that satisfy a + b + c = p.
        If no triplet exists, returns 0, 0, 0.
    """

    # loop through values for a
    for a in range(1, p):

        # loop through values for b
        for b in range(1, p):

            # faster way to evaluate c
            c = p - a - b

            # test if a valid triple is found
            if (a ** 2 + b ** 2) == c ** 2:
                return a, b, c

    return 0, 0, 0


a, b, c = pythagorean_triplet(LIMIT)

print(f"a: {a}, b: {b}, c: {c}")
print(f"Sum = {a + b + c}")
print(f"Product = {a * b * c}")
