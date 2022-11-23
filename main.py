import multiprocessing

import solve_GUI
import test_boards
import solver


class Process(multiprocessing.Process):
    def __init__(self, proc_id, matrix):
        super(Process, self).__init__()
        self.id = proc_id
        self.matrix = matrix

    def run(self):
        if self.id == 0:
            solve_GUI.run_GUI(self.matrix)
        if self.id == 1:
            print("welcome To Kim's sudoku solver")
            solver.print_matrix(self.matrix)
            is_solvable = solver.start_matrix_solve(self.matrix)
            solver.print_matrix(self.matrix)
            print(is_solvable[1])


if __name__ == '__main__':
    matrix_to_solve = test_boards.T_1

    p0 = Process(0, matrix_to_solve)
    p0.start()
    p1 = Process(1, matrix_to_solve)
    p1.start()
    p0.join()
    p1.join()
