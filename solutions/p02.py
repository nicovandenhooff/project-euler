# Project Euler: Problem 2
# Even Fibonacci Numbers
# Author: Nico Van den Hooff
# Github: https://github.com/nicovandenhooff/project-euler
# Problem: https://projecteuler.net/problem=2


LIMIT = 4000000
N1 = 0
N2 = 1


def fibonacci(n1, n2):
    """Simple value to calculate the next two values in a fibonacci sequence.

    Parameters
    ----------
    n1 : int
        The first previous value in the sequence.
    n2 : int
        The second previous value in the sequence.

    Returns
    -------
    (n1, n2) : (int, int)
        The next two values in the fibonacci sequence
    """
    temp = n2
    n2 += n1
    n1 = temp

    return n1, n2


def sum_even_fibs(limit, result, n1_start=0, n2_start=1):
    """Calculates the sum of a sequence of fibonacci numbers.

    Parameters
    ----------
    limit : int
        The upper limit to sum until.
    result: str
        Whether to sum "all", "odd", or "even" fibonacci values.
    n1_start : int, optional
        The first number in the fibonacci sequence, by default 0.
    n2_start : int, optional
        The second number in the fibonacci sequence, by default 1.

    Returns
    -------
    total : int
        The sum of the desired fibonacci numbers.
    """
    total = 0

    # get the first two fibonacci numbers
    n1, n2 = fibonacci(n1_start, n2_start)

    # continue getting fibonacci numbers until limit is reached
    while n2 < limit:
        n1, n2 = fibonacci(n1, n2)

        # add to respective sum
        if result == "all":
            total += n2
        elif result == "even" and n2 % 2 == 0:
            total += n2
        elif result == "odd" and n2 % 2 != 0:
            total += n2

    return total


print(sum_even_fibs(LIMIT, "even", N1, N2))
