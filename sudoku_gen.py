import solver
import test_boards
import random


def get_sudoku(k):
    try:
        import numpy as np
        print("generating new sudoku using numpy")
        return gen_sudoku(k)
    except ModuleNotFoundError:
        print("generating new sudoku without numpy")
        return gen_nonnp_sudoku(k)


def gen_nonnp_rnd_board():
    t = test_boards.T_full
    k = 5
    for i in range(0, 2 * k):
        t = shuffle_matrix(t)
        t = flip_matrix(t)

    return t


def flip_matrix(matrix):
    flipped_mat = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                   ]
    for i in range(0, 9):
        for j in range(0, 9):
            flipped_mat[i][j] = matrix[j][i]
    return flipped_mat


def shuffle_matrix(matrix):
    m1, m2, m3 = matrix[0:3], matrix[3:6], matrix[6:9]
    random.shuffle(m1)
    random.shuffle(m2)
    random.shuffle(m3)
    matrix[0:3], matrix[3:6], matrix[6:9] = m1, m2, m3
    return matrix


def gen_rnd_board():
    import numpy as np
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
    import numpy as np
    matrix = gen_rnd_board()
    solver.print_matrix(matrix)
    matrix = matrix.reshape(1, 81)
    i = 0
    m = 81 - k
    while k > 0:
        r = np.random.randint(0, m + k)
        if r > k:
            m -= 1
        else:
            k -= 1
            matrix[0][i] = 0
        i += 1
    return matrix.reshape(9, 9)


def gen_nonnp_sudoku(k):
    matrix = gen_nonnp_rnd_board()
    i = 0
    m = 81 - k
    while k > 0 and i < 81:
        r = random.randint(0, m + k)
        if r >= k:
            m -= 1
        else:
            k -= 1
            matrix[i // 9][i % 9] = 0
        i += 1
    return matrix
