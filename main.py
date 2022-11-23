import time
import test_boards
import solver
import play_GUI

if __name__ == '__main__':
    matrix_to_solve = test_boards.T_1
    solver.print_matrix(matrix_to_solve)
    t0 = time.time()
    is_solvable = solver.start_matrix_solve(matrix_to_solve)
    t1 = time.time()
    print()
    solver.print_matrix(matrix_to_solve)
    print(is_solvable)
    print(t1 - t0)
