# Project Euler: Problem 17
# Large sum
# Author: Nico Van den Hooff
# Github: https://github.com/nicovandenhooff/project-euler
# Problem: https://projecteuler.net/problem=17

# Note: This could likely be done with a combinatorics solution,
#       but I decided to brute force it for fun so that I could
#       practice working with logic and strings.


# dictionary of numbers and words needed to represent
# the first 1000 numbers in words
numbers = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand",
}


def num_digits(n):
    """Counts the number of digits in a number.

    Parameters
    ----------
    n : int
        The number.

    Returns
    -------
    int
        The number of digits.
    """
    return len(str(n))


def extract_digits(n):
    """Simple function to return a tuple of digits for each
    digit in a number.

    Parameters
    ----------
    n : int
        The number, for example 793.

    Returns
    -------
    tuple of int
        Tuple of digits, for example (7, 9, 3)
    """
    return tuple(int(digit) for digit in str(n))


def string_words(start, stop):
    """Converts a range of numbers from 1 up to 1000 from numbers
    to their string equivalent.

    Parameters
    ----------
    start : int
        The starting value, must be >= 1.
    stop : int
        The ending value, must be <= 1000.

    Returns
    -------
    words: list of str
        A list of string representations of each number.
    """
    # the word list
    words = []

    for i in range(start, stop):
        digit_string = ""

        # if between 1-20 append dictionary value
        if i in range(1, 21):
            words.append(numbers[i])

        # two digit numbers
        elif num_digits(i) == 2:

            # extract individual digits
            first, second = extract_digits(i)

            # if second digit is zero append dictionary value
            if second == 0:
                words.append(numbers[i])

            # othewise append two digit string representation
            else:
                digit_string += numbers[first * 10]
                digit_string += numbers[second]
                words.append(digit_string)

        # three digit numbers
        elif num_digits(i) == 3:

            # extract individual digits
            first, second, third = extract_digits(i)

            # "num" + "hundred"
            digit_string += numbers[first]
            digit_string += numbers[100]

            # if second, third, digits are zero append result
            if second == 0 and third == 0:
                words.append(digit_string)

            # if second is zero, append "and" + respective number
            elif second == 0:
                digit_string += "and"
                digit_string += numbers[third]
                words.append(digit_string)

            # if second is one, append "and" + respective teens number
            elif second == 1:
                digit_string += "and"
                digit_string += numbers[third + 10]
                words.append(digit_string)

            # if second not zero but third is append "and" and multiple of 10
            elif second != 0 and third == 0:
                digit_string += "and"
                digit_string += numbers[second * 10]
                words.append(digit_string)

            # otherwise append three digit string representation
            else:
                digit_string += "and"
                digit_string += numbers[second * 10]
                digit_string += numbers[third]
                words.append(digit_string)

        # four digit numbers - got lazy here lol
        else:
            digit_string += numbers[1]
            digit_string += numbers[1000]
            words.append(digit_string)

    return words


print(len("".join(string_words(1, 1001))))
