# Project Euler: Problem 11
# Largest Product in a Grid
# Author: Nico Van den Hooff
# Github: https://github.com/nicovandenhooff/project-euler
# Problem: https://projecteuler.net/problem=11

# Note: The goal for this problem is to find the largest consecutive product in
#       an n x n grid, where you can move k spaces up, down, left, right or
#       diagonal


consecutive = 4

# 20 x 20 grid
grid = [
    [8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
    [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
    [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
    [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
    [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
    [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
    [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
    [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
    [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
    [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
    [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
    [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
    [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
    [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
    [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
    [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
    [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
    [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
    [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
    [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48],
]


def largest_product(grid, consecutive):
    """Calculates the largest product for a square n x n grid for k consecutive
    numbers in the same direction.

    To find this product, the function iterates through each number in the grid,
    performing multiplications for k consecutive numbers in the following directions,
    if they are valid:
        1) Down
        2) Right
        3) Diagonal down and rightward
        4) Diagonal down and leftwards

    The method is designed carefully to iterate over indicies carefully so that
    multiplications in the direction up, left, diagonal up and rightward, or
    diagonal up and leftward would be the exact same as their counter parts
    in the above numeric list, respectively.

    Parameters
    ----------
    grid : 2d list of int
        The n x n grid
    consecutive : int
        The number of consecutive numbers to multiply, strictly <= n

    Returns
    -------
    largest : int
        The largest consecutive product
    """
    total_rows = len(grid)
    total_columns = len(grid[0])

    # valid indicies to perform calculation over
    valid_rows = total_rows - consecutive
    valid_columns = total_columns - consecutive

    # initialize largest value
    largest = -1

    for i in range(total_rows):
        for j in range(total_columns):

            # calculate product in downwards direction if row is in range
            if i <= valid_rows:
                largest = max(calc_product(grid, i, j, "down", consecutive), largest)

            # calculate product in rightwards  direction if column is in range
            if j <= valid_columns:
                largest = max(calc_product(grid, i, j, "right", consecutive), largest)

            # calculate product in diagonal down-right direction if row/column are in range
            if i <= valid_rows and j <= valid_columns:
                largest = max(calc_product(grid, i, j, "diagR", consecutive), largest)

            # calculate product in diagonal down-left direction if row/column are in range
            if i <= valid_rows and j >= consecutive - 1:
                largest = max(calc_product(grid, i, j, "diagL", consecutive), largest)

    return largest


def calc_product(grid, row, column, direction, consecutive):
    """Calculates a consecutive product for a given row, column location
    in an n x n grid for the desired direction.

    Parameters
    ----------
    grid : 2d list of int
        The n x n grid.
    row : int
        The row location.
    column : int
        The column location.
    direction : str
        The direction to perform the product.
        Must equal: "down", "right", "diagR", or "diagL"
    consecutive : int
        The consecutive multiplications to perform,

    Returns
    -------
    result : int
        The consecutive product.
    """
    # starting location
    result = grid[row][column]

    # downwards consecutive product
    if direction == "down":
        for n in range(1, consecutive):
            result *= grid[row + n][column]

    # rightwards consecutive product
    if direction == "right":
        for n in range(1, consecutive):
            result *= grid[row][column + n]

    # diagonal down and rightwards consecutive product
    if direction == "diagR":
        for n in range(1, consecutive):
            result *= grid[row + n][column + n]

    # diagonal down and leftwards consecutive product
    if direction == "diagL":
        for n in range(1, consecutive):
            result *= grid[row + n][column - n]

    return result


# print the answer
print(largest_product(grid, consecutive))
