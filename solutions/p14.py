# Project Euler: Problem 14
# Longest Collatz Sequence
# Author: Nico Van den Hooff
# Github: https://github.com/nicovandenhooff/project-euler
# Problem: https://projecteuler.net/problem=14

# Note: Being a simple problem, I decided to brute force this
#       with a straight forward algorithm.  Takes about ~20
#       seconds on my laptop.


def next_integer(n):
    """Generates the next integer in a Collatz sequence.

    Parameters
    ----------
    n : int
        The most recent integer in the sequence.

    Returns
    -------
    int
        The next integer in the sequence.
    """
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def generate_sequence(n):
    """Generates a Collatz Sequence starting at a given number.

    Note, this assumes that all Collatz Sequence's stop at 1.

    Parameters
    ----------
    n : int
        The number to start the sequence at.

    Returns
    -------
    sequence : list of int
        The Collatz Sequence.
    """

    sequence = []

    # generate sequence
    while n != 1:
        sequence.append(n)
        n = next_integer(n)

    # append 1 to sequence since all sequences assumed to end in 1
    sequence.append(1)

    return sequence


def longest_sequence(start=1, end=1000000):
    """Determines the largest Collatz sequence for a range of values.

    Parameters
    ----------
    start : int, optional
        The first value to calculate a sequence for, by default 1.
    end : int, optional
        The value to calculate sequences until, by default 1000000.

    Returns
    -------
    max_length, max_start_value : int, int
        The longest sequence length and the starting value for this sequence.
    """

    max_length = 0
    max_start_value = 0

    # generate sequence for each value
    for i in range(start, end):
        current = generate_sequence(i)

        # if the current sequence is the longest, update values
        if len(current) > max_length:
            max_length = len(current)
            max_start_value = i

    return max_length, max_start_value


max_length, max_start_value = longest_sequence()
print(max_start_value)
print(max_length)
