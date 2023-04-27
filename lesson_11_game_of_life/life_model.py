"""Model of the game.
Contains some patterns, functions with rules for game."""

import random
import time

"""Size of window for game (cells)."""

x = 25
y = 25


def matrix_start(x=x, y=y, gen=0):
    """Creates matrix (x * y cells)."""

    matrix = [gen] * x
    for i in range(y):
        matrix[i] = [gen] * y
    return matrix


def random_matrix(matrix, x=x, y=y):
    """Creates random matrix (size == x * y cells)."""

    for i in range(x):
        for j in range(y):
            matrix[i][j] = random.randint(0, 1)
    return matrix


def create_new_matrix():
    """Creates new matrix.
    Uses current matrix with rules for born cell, go life cell or die cell.
    In gen_list counts generation of every cell's life (for color it).
    Detects the execution time"""

    global res  # for showtime result
    start = time.time()

    count = 0
    global matrix
    global new_matrix
    global gen_list
    for i in range(x):
        for j in range(y):
            count = count_neighbors(matrix, i, j)
            if matrix[i][j] == 0:
                gen_list[i][j] = 0
                if count < 2:
                    new_matrix[i][j] = 0
                if count == 3 or count == 2:
                    new_matrix[i][j] = 1
                if count >= 4:
                    new_matrix[i][j] = 0
            if matrix[i][j] == 1:
                gen_list[i][j] = gen_list[i][j] + 1
                if count == 2 or count == 3:
                    new_matrix[i][j] = 1
                if count < 2 or count > 3:
                    new_matrix[i][j] = 0

    step = matrix
    matrix = new_matrix
    new_matrix = step
    end = time.time()
    res = end - start
    return matrix


def count_neighbors(grid, row, col):
    """Counts neighbors for every cell.
    This configuration provides a transition from one side to the other for the extreme cells."""

    count = 0
    if (row - 1 >= 0) and (col - 1 >= 0):
        count = count + grid[row - 1][col - 1]
    if (row - 1 < 0) and (col - 1 >= 0):
        count = count + grid[x - 1][col - 1]
    if (row - 1 >= 0) and (col - 1 < 0):
        count = count + grid[row - 1][y - 1]
    if (row - 1 < 0) and (col - 1 < 0):
        count = count + grid[x - 1][y - 1]

    if (col - 1 >= 0):
        count = count + grid[row][col - 1]
    if (col - 1 < 0):
        count = count + grid[row][y - 1]

    if (row + 1 > (x - 1)) and (col - 1 < 0):
        count = count + grid[0][y - 1]
    if (row + 1 > (x - 1)) and (col - 1 >= 0):
        count = count + grid[0][col - 1]
    if (row + 1 <= (x - 1)) and (col - 1 < 0):
        count = count + grid[row + 1][y - 1]
    if (row + 1 <= (x - 1)) and (col - 1 >= 0):
        count = count + grid[row + 1][col - 1]

    if (row - 1 >= 0):
        count = count + grid[row - 1][col]
    if (row - 1 < 0):
        count = count + grid[x - 1][col]

    if (row + 1 > (x - 1)):
        count = count + grid[0][col]
    if (row + 1 <= (x - 1)):
        count = count + grid[row + 1][col]

    if (row - 1 < 0) and (col + 1 > (y - 1)):
        count = count + grid[x - 1][0]
    if (row - 1 >= 0) and (col + 1 > (y - 1)):
        count = count + grid[row - 1][0]
    if (row - 1 < 0) and (col + 1 <= (y - 1)):
        count = count + grid[x - 1][col + 1]
    if (row - 1 >= 0) and (col + 1 <= (y - 1)):
        count = count + grid[row - 1][col + 1]

    if (col + 1 > (y - 1)):
        count = count + grid[row][0]
    if (col + 1 <= (y - 1)):
        count = count + grid[row][col + 1]

    if (row + 1 > (x - 1)) and ((col + 1) > (y - 1)):
        count = count + grid[0][0]
    if (row + 1 <= (x - 1)) and ((col + 1) > (y - 1)):
        count = count + grid[row + 1][0]
    if (row + 1 <= (x - 1)) and ((col + 1) <= (y - 1)):
        count = count + grid[row + 1][col + 1]
    if (row + 1 > (x - 1)) and ((col + 1) <= (y - 1)):
        count = count + grid[0][col + 1]

    return count


def make_count_list(matrix):
    """Makes count_list of neighbors for every cell."""

    global count_list
    for i in range(x):
        for j in range(y):
            count_list[i][j] = count_neighbors(matrix, i, j)


glider_pattern = [[0, 0, 0, 0, 0],
                  [0, 1, 1, 0, 0],
                  [0, 0, 0, 1, 0],
                  [0, 1, 1, 1, 0],
                  [0, 0, 0, 0, 0]]

glider_gun_pattern = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


# def turn_in_int(pattern):
#     for i in len(pattern):
#         for j in len(pattern[i]):
#             pattern[i][j] = int(pattern[i][j])
#
# glider_gun_pattern = turn_in_int(glider_gun_pattern)

def load_pattern(pattern, x_offset=0, y_offset=0):
    """Add pattern in matrix with indentation x y."""

    global matrix
    matrix = matrix_start()
    j = y_offset
    for row in pattern:
        i = x_offset
        for value in row:
            matrix[i][j] = value
            i = i + 1
        j = j + 1


matrix = matrix_start(x, y)
new_matrix = matrix_start(x, y)
gen_list = matrix_start(x, y)
count_list = matrix_start(x, y)
res = 0


def main():
    random_matrix(matrix)
    for i in range(10):
        print(matrix)
        print(res)


if __name__ == '__main__':
    main()
