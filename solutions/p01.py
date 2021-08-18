# Project Euler: Problem 1
# Multiples of 3 or 5
# Author: Nico Van den Hooff
# Github: https://github.com/nicovandenhooff/project-euler
# Problem: https://projecteuler.net/problem=1


def sum_multiples(n1, n2, upper_limit):
    """Calculates the sum from 0 to an upper limit n for all
    multiples of two numbers.

    Parameters
    ----------
    n1 : int
        The first multiple.
    n2 : int
        The second multiple.
    upper_limit : int
        The upper limit to stop the summation at.

    Returns
    -------
    total : int
        The summation of all multiples of num1 and/or num2
        from 0 to n.
    """
    total = 0

    for i in range(upper_limit):
        # check for multiples
        if i % n1 == 0 or i % n2 == 0:
            total += i

    return total


# print the answer
print(sum_multiples(3, 5, 1000))
