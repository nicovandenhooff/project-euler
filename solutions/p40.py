# Project Euler: Problem 40
# Champernowne's constant
# Author: Nico Van den Hooff
# Github: https://github.com/nicovandenhooff/project-euler
# Problem: https://projecteuler.net/problem=40

# Note : Solution is brute force but runs in ~0.1 seconds on my laptop,
# which is satisfactory for me :).

# the length of the sequence to generate
LENGTH = 1000000

# the indices to multiply
INDICIES = [1, 10, 100, 1000, 10000, 100000, 1000000]


def generate_sequence(length, indicies):
    """Generates an irrational decimal fraction by concatenating
    the positive integers until a desired length of number is reached.

    Then, calculates the product of the digits at desired indicies.

    Parameters
    ----------
    length : int
        The length of the sequence to generate.
    indicies : list of int
        The indicies to multiply.

    Returns
    -------
    digits, product : list of int, int
        The digits at the given indices and the prodct of these digits.
    """

    # the next integer to concatenate
    counter = 1

    # the sequences
    sequence = ""

    # the digits at the desired indicies
    digits = []

    # initialize the product to 1
    product = 1

    # generate the irrational number
    while len(sequence) < length:
        sequence = sequence + str(counter)
        counter += 1

    # get the digits at each index
    for idx in indicies:
        digits.append(sequence[idx - 1])

    # calculate the product
    for digit in digits:
        product *= int(digit)

    return digits, product


print(generate_sequence(LENGTH, INDICIES))
