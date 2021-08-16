# Project Euler: Problem 22
# Names scores
# Author: Nico Van den Hooff
# Github: https://github.com/nicovandenhooff/project-euler
# Problem: https://projecteuler.net/problem=22

# Note: I implement a vectorized implementation with NumPy for this problem.
#       Specifically, I first create a vector for each name, where the vectors
#       shape is (26, 1).  Each position in the vector is then filled with the
#       number of times a letter shows up in a given name.  I then combine all
#       of the vectors into a names matrix, which is of shape (5163, 26).  Next,
#       I simply multiply the matrix by a points vector of shape (26, 1), which
#       gives us a vector of shape (5163, 1) that represents the points value
#       for each persons name.  Finally, I multiply the points value vector by
#       a "position" vector of shape (5163, 1) that represents each position a
#       name has in the list (element-wise multiplication here).  To get the
#       answer, the sum is taken over the final vector.


import string
import numpy as np
import csv

# path to the names text file
PATH = "./project-euler/data/p022_names.txt"


def get_names_list(path):
    """Creates a sorted list of names and a "positions" vector.

    Parameters
    ----------
    path : str
        The path of the names .txt file.

    Returns
    -------
    names, positions : list of str, numpy array
        The names list and positions vector.  The positions vector
        has shape (1, number of names).
    """
    # the names list
    names = []

    # read in names
    with open(path) as f:
        for row in csv.reader(f):
            names.extend(row)

    # sort names
    names.sort()

    # create positions vector
    positions = np.arange(1, len(names) + 1)

    return names, positions


def create_names_matrix(names, vector_shape=(26,), start=1, stop=27):
    """Creates a names matrix and points vector.

    Parameters
    ----------
    names : list of str
        The list of names.
    vector_shape : int, optional
        The shape of each name vector, by default (26,).
    start : int, optional
        Starting points value (inclusive), by default 1.
    stop : int, optional
        Ending points value (exclusive), by default 27.

    Returns
    -------
    names_matrix, points : 2D numpy array, 1D numpy array
        The names matrix and points vector.
    """

    # to store the vectorized names
    vectorized_names = []

    # the points vector
    points = np.arange(start, stop)

    # dictionary mapping letters to points
    char_to_points = dict(zip(string.ascii_uppercase, range(start, stop)))

    # vectorize each name
    for name in names:
        vector = np.zeros(vector_shape)
        for char in name:
            # have to be careful with indexing here
            index = char_to_points[char]
            vector[index - 1] += 1

        # append each name to vectorized names list
        vectorized_names.append(vector)

    # create names matrix from vectors
    names_matrix = np.array(vectorized_names)

    return names_matrix, points


names, positions = get_names_list(PATH)
names_matrix, points = create_names_matrix(names)
print(np.sum(np.matmul(names_matrix, points) * positions))
