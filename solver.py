import time
from asyncio import sleep


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


def check_new_entry(matrix, val, c, r):
    for i in range(9):
        if matrix[i][c] == val and i != r:
            return False
    for j in range(9):
        if matrix[r][j] == val and j != c:
            return False
    for i in range(c - c % 3, c - c % 3 + 3):
        for j in range(r - r % 3, r - r % 3 + 3):
            if i == c and j == r: continue
            if matrix[j][i] == val:
                return False
    return True


def solve_matrix(matrix, c, r):
    if matrix[r][c] == 9:
        matrix[r][c] = 0
        return False

    matrix[r][c] += 1
    if check_new_entry(matrix, matrix[r][c], c, r):
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


def start_matrix_solve(matrix):
    (i, j) = find_empty(matrix)
    if (i, j) == (9, 9):
        return matrix, True
    else:
        return matrix, solve_matrix(matrix, j, i)
