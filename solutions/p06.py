# Project Euler: Problem 6
# Sum sqaure difference
# Author: Nico Van den Hooff
# Github: https://github.com/nicovandenhooff/project-euler
# Problem: https://projecteuler.net/problem=6


import numpy as np


START = 1
STOP = 101
NUMBERS = [x for x in range(START, STOP)]


def sum_of_squares(numbers):
    """Calculates the sum of squares for a set of numbers.
    (This is just the dot product).

    Parameters
    ----------
    numbers : list of int
        The set of numbers.

    Returns
    -------
    int
        The sum of squares.
    """
    vector = np.array(numbers)

    return np.dot(vector, vector)


def square_of_sum(numbers):
    """Calculates the square of the sum of a set of numbers.

    Parameters
    ----------
    numbers : list of int
        The set of numbers.

    Returns
    -------
    int
        The square of the sum.
    """
    vector = np.array(numbers)

    return np.square(np.sum(vector))


# calculate each value
sum_sqaures = sum_of_squares(NUMBERS)
square_sum = square_of_sum(NUMBERS)
difference = square_sum - sum_sqaures

print("The numbers are: " + str(NUMBERS))
print("The square of the sum is: " + str(square_sum))
print("The sum of squares is: " + str(sum_sqaures))
print("The difference is: " + str(difference))
