# Project Euler: Problem 29
# Distict powers
# Author: Nico Van den Hooff
# Github: https://github.com/nicovandenhooff/project-euler
# Problem: https://projecteuler.net/problem=29

# Note: Very fast in python thanks to the efficient set class.


def distinct_powers(start, stop):
    """Calculates the distinct powers in the sequence a^b for:
        start <= a <= stop
        start <= b <= stop

    Parameters
    ----------
    start : int
    stop : int

    Returns
    -------
    int
        The number of distinct powers.
    """
    # set to hold distinct powers
    distinct = set()

    # find distinct powers
    for a in range(start, stop):
        for b in range(start, stop):
            distinct.add(a ** b)

    return len(distinct)


print(distinct_powers(2, 101))
