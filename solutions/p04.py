# Project Euler: Problem 4
# Largest palindrome product
# Author: Nico Van den Hooff
# Github: https://github.com/nicovandenhooff/project-euler
# Problem: https://projecteuler.net/problem=4


def is_palindrome(num):
    """Determines if a number is a palindrome.

    Parameters
    ----------
    num : int
        The number in question.

    Returns
    -------
    bool
        True if the number is a palindrome, False otherwise.
    """
    # number as it is
    forward = str(num).replace("-", "")

    # number reversed
    backward = forward[::-1]

    return forward == backward


def largest_palindrome(start):
    """Finds the largest palindrome for the product of two
    n digit numbers.

    Parameters
    ----------
    start : int
        The power to raise 10 too, to start at.  For example
        to find the largest palindrome for two 3 digit numbers,
        start = 2 since 10^2 = 100, the first 3 digit number.

    Returns
    -------
    largest : int
        The largest palindrome.
    """

    # number of digits
    digits = start + 1

    # starting value
    num1 = num2 = 10 ** start

    # largest palindrome
    largest = 0

    # loop through first number while digits are valid
    while len(str(num1)) == digits:

        # loop through second number while digits are valid
        while len(str(num2)) == digits:
            product = num1 * num2

            # if palindrome compare to previous largest
            if is_palindrome(product):
                largest = max(product, largest)

            num2 += 1

        num1 += 1
        num2 = 10 ** start  # reset second number

    return largest


# print the answer
print(largest_palindrome(2))
