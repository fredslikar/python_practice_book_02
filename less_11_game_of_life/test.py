import random
import time

x = 100
y = 100
num_gen = 2


def matrix_start(x=x, y=y, gen=0):
    start = time.time()
    matrix = [gen] * x
    for i in range(x):
        matrix[i] = [gen] * x
    end = time.time()
    res_matrix_start = end - start
    print('res_matrix_start = ', res_matrix_start)
    return matrix



def random_matrix(matrix, x=x, y=y):
    start = time.time()
    for i in range(x):
        for j in range(y):
            matrix[i][j] = random.randint(0, 1)
    end = time.time()
    res_random_matrix = end - start
    print('res_random_matrix = ', res_random_matrix)
    return matrix



def create_new_matrix():
    start = time.time()
    count = 0
    global matrix
    global new_matrix
    for i in range(0, x):
        for j in range(0, y):
            count = count_neighbors(matrix, i, j)
    end = time.time()
    step = matrix
    matrix = new_matrix
    new_matrix = step


    res_create_new_matrix = end - start
    print('res_create_new_matrix = ', res_create_new_matrix)
    return matrix


def count_neighbors(grid, row, col):
    count = 0
    if (row-1 >= 0) and (col-1 >= 0):
        count = count + grid[row-1][col-1]
    if (row-1 < 0) and (col-1 >= 0):
        count = count + grid[x-1][col-1]
    if (row-1 >= 0) and (col-1 < 0):
        count = count + grid[row-1][y-1]
    if (row-1 < 0) and (col-1 < 0):
        count = count + grid[x-1][y-1]

    if (col - 1 >= 0):
        count = count + grid[row][col - 1]
    if (col - 1 < 0):
        count = count + grid[row][y-1]

    if (row+1 > (x-1)) and (col-1 < 0):
        count = count + grid[0][y-1]
    if (row+1 > (x-1)) and (col-1 >= 0):
        count = count + grid[0][col-1]
    if (row+1 <= (x-1)) and (col-1 < 0):
        count = count + grid[row+1][y-1]
    if (row+1 <= (x-1)) and (col-1 >= 0):
        count = count + grid[row+1][col-1]

    if (row - 1 >= 0):
        count = count + grid[row-1][col]
    if (row - 1 < 0):
        count = count + grid[x-1][col]

    if (row + 1 > (x-1)):
        count = count + grid[0][col]
    if (row + 1 <= (x-1)):
        count = count + grid[row+1][col]

    if (row - 1 < 0) and (col + 1 > (y-1)):
        count = count + grid[x-1][0]
    if (row - 1 >= 0) and (col + 1 > (y-1)):
        count = count + grid[row-1][0]
    if (row - 1 < 0) and (col + 1 <= (y-1)):
        count = count + grid[x-1][col+1]
    if (row - 1 >= 0) and (col + 1 <= (y-1)):
        count = count + grid[row-1][col+1]

    if (col + 1 > (y-1)):
        count = count + grid[row][0]
    if (col + 1 <= (y-1)):
        count = count + grid[row][col+1]

    if (row + 1 > (x-1)) and ((col + 1) > (y-1)):
        count = count + grid[0][0]
    if (row + 1 <= (x-1)) and ((col + 1) > (y-1)):
        count = count + grid[row+1][0]
    if (row + 1 <= (x-1)) and ((col + 1) <= (y-1)):
        count = count + grid[row+1][col+1]
    if (row + 1 > (x-1)) and ((col + 1) <= (y-1)):
        count = count + grid[0][col+1]

    return count


glider_pattern = [[0, 0, 0, 0, 0],
                  [0, 1, 1, 0, 0],
                  [0, 0, 0, 1, 0],
                  [0, 1, 1, 1, 0],
                  [0, 0, 0, 0, 0]]

glider_gun_pattern = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
gen_list = matrix_start(gen=num_gen)

create_new_matrix()


