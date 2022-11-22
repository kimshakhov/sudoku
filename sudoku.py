from array import *
import time
import random
import copy
from timeit import timeit

T_1 = [
    [0, 0, 1, 0, 7, 0, 0, 9, 3],
    [0, 6, 0, 4, 0, 0, 0, 0, 0],
    [0, 2, 7, 0, 0, 0, 6, 0, 5],
    [0, 1, 0, 0, 6, 9, 0, 0, 0],
    [0, 0, 0, 1, 0, 4, 0, 6, 2],
    [0, 0, 3, 0, 0, 0, 9, 0, 0],
    [1, 7, 0, 0, 5, 6, 2, 3, 8],
    [9, 8, 0, 3, 4, 7, 1, 0, 6],
    [5, 3, 0, 2, 0, 0, 0, 0, 0],
]
T_2 = [
    [8, 9, 0, 1, 0, 0, 0, 4, 0],
    [0, 2, 0, 0, 0, 0, 8, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 0, 1, 5, 0, 0, 0, 0, 0],
    [0, 0, 0, 9, 0, 0, 6, 0, 7],
    [0, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 2, 8, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 0, 0, 6, 0, 0, 0, 0],
]
T_3 = [
    [8, 0, 0, 1, 0, 0, 0, 4, 0],
    [0, 2, 0, 0, 0, 0, 8, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 0, 1, 5, 0, 0, 0, 0, 0],
    [0, 0, 0, 9, 0, 0, 6, 0, 7],
    [0, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 2, 8, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 0, 0, 6, 0, 0, 0, 0],
]
T_4 = [
    [0, 0, 0, 1, 0, 0, 0, 4, 0],
    [0, 2, 0, 0, 0, 0, 8, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 0, 1, 5, 0, 0, 0, 0, 0],
    [0, 0, 0, 9, 0, 0, 6, 0, 7],
    [0, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 2, 8, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 0, 0, 6, 0, 0, 0, 0],
]

T_empty = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]


def print_matrix(matrix):
    countdown = 0
    countright = 0
    print()
    print()
    for r in matrix:
        for c in r:
            print(c, end=" ")
            countright += 1
            if countright % 3 == 0: print('|', end=" ")
        print()
        countdown += 1
        if countdown % 3 == 0: print("----- | ----- | -----")


def check_new_entry(matrix, c, r):
    new = matrix[r][c]
    # print('checking new entry {} at {}{}',new, r,c)
    for i in range(9):
        if matrix[i][c] == new and i != r:
            return False
    for j in range(9):
        if matrix[r][j] == new and j != c:
            return False
    for i in range(c - c % 3, c - c % 3 + 3):
        for j in range(r - r % 3, r - r % 3 + 3):
            if i == c and j == r: continue
            if matrix[j][i] == new:
                return False
    # print("accepted")
    return True


# global steps
# steps = 0
def solve_matrix(matrix, c, r):
    # pr = random.randint(0, 10000)
    # if pr == 13: print_matrix(matrix)

    if matrix[r][c] == 9:
        matrix[r][c] = 0
        return False
    # global steps
    # steps+=1
    matrix[r][c] += 1
    if check_new_entry(matrix, c, r):
        (i, j) = find_empty(matrix)
        if (i, j) == (9, 9) or solve_matrix(matrix, j, i):
            return True
        else:
            return solve_matrix(matrix, c, r)
    else:
        return solve_matrix(matrix, c, r)


def find_empty(matrix):
    i, j = 0, 0
    while i < 9 and j < 9:
        if matrix[i][j] == 0:
            return (i, j)
        if j != 8:
            j, i = j + 1, i
        elif i != 8:
            j, i = 0, i + 1
        else:
            return (9, 9)


def invert_matrix(matrix, inv_matrix):
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0:
                options = 0
                k = 1
                while k < 10:
                    matrix[i][j] = k
                    if check_new_entry(matrix, i, j):
                        options += 1
                    matrix[i][j] = 0
                    k += 1
                inv_matrix[i][j] = options
                print('assigned ' + str(options) + ' to ' + str(i) + str(j))
            else:
                inv_matrix[i][j] = 0
    print_matrix(inv_matrix)
    print_matrix(matrix)
    return inv_matrix


def start_matrix_solve(matrix):
    (i, j) = find_empty(matrix)
    if (i, j) == (9, 9):
        return True
    else:
        return solve_matrix(matrix, j, i)


matrix_to_solve = T_1
print_matrix(matrix_to_solve)
t0 = time.time()
is_solvable = start_matrix_solve(matrix_to_solve)
# inv_matrix = (T_empty)
# inv_matrix = invert_matrix(matrix_to_solve, inv_matrix)
t1 = time.time()
print()
print_matrix(matrix_to_solve)
# print_matrix(inv_matrix)
print(is_solvable)
# print(steps)
print(t1 - t0)
