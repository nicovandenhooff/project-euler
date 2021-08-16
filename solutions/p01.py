# Project Euler: Problem 1
# Multiples of 3 or 5
# Author: Nico Van den Hooff
# Github: https://github.com/nicovandenhooff/project-euler
# Problem: https://projecteuler.net/problem=1


def sum_multiples(num1, num2, upper_limit):
    """Calculates the sum from 0 to an upper limit n for all
    multiples of two numbers.

    Parameters
    ----------
    num1 : int
        The first multiple.
    num2 : int
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

    for num in range(upper_limit):
        # add to total if divisible by both numbers
        if num % num1 == 0 and num % num2 == 0:
            total += num

        # add to total if only divisible by first number
        elif num % num1 == 0:
            total += num

        # add to total if only divisible by second number
        elif num % num2 == 0:
            total += num

    return total


# print the answer
print(sum_multiples(3, 5, 1000))
