import solver
import test_boards
import numpy as np


def gen_rnd_board():
    rng = np.random.default_rng()
    t = np.array(test_boards.T_full)
    for i in range(0, 5):
        col_idx1 = np.array([0, 1, 2])
        col_idx2 = np.array([3, 4, 5])
        col_idx3 = np.array([6, 7, 8])
        rng.shuffle(col_idx1)
        rng.shuffle(col_idx2)
        rng.shuffle(col_idx3)
        col_idx = np.concatenate((col_idx1, col_idx2, col_idx3), axis=None)
        row_idx1 = np.array([0, 1, 2])
        row_idx2 = np.array([3, 4, 5])
        row_idx3 = np.array([6, 7, 8])
        rng.shuffle(row_idx1)
        rng.shuffle(row_idx2)
        rng.shuffle(row_idx3)
        row_idx = np.concatenate((row_idx1, row_idx2, row_idx3), axis=None)
        t = t[row_idx, :]
        t = t[:, col_idx]
    return t


def gen_sudoku(k):
    matrix = gen_rnd_board()
    print("got matrix")
    solver.print_matrix(matrix)
    matrix = matrix.reshape(1, 81)
    i = 0
    m = 81 - k
    while k > 0:
        r = np.random.randint(0, m + k)
        if r >= k:
            m -= 1
        else:
            k -= 1
            matrix[0][i] = 0
        i += 1
    return matrix.reshape(9, 9)
