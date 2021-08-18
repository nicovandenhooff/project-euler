# Project Euler: Problem 15
# Lattice paths
# Author: Nico Van den Hooff
# Github: https://github.com/nicovandenhooff/project-euler
# Problem: https://projecteuler.net/problem=15

# For this problem I found it helpful to first read this wiki
# article: https://en.wikipedia.org/wiki/Lattice_path
# Combinatorics can be used to count lattice paths, through the
# use of a binomial coefficient.  Specifically, if we start at
# location (0, 0) and go to location (n, k) in a grid, the #
# of lattice paths is (n + k) choose k, or equivalently:
# n! / k!(n-k!)

from math import comb


def count_lattice_paths(n, k):
    """Counts the number of lattice paths from (0, 0) to (n, k)

    Parameters
    ----------
    n : int
        x coordinate
    k : int
        y coordinate

    Returns
    -------
    int
        The number of lattice paths
    """
    return comb((n + k), n)


print(count_lattice_paths(20, 20))
