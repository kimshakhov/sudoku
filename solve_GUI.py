import multiprocessing

import pygame
import solver
import time
import test_boards

pygame.font.init()
win = pygame.display.set_mode((550, 700))
fnt = pygame.font.SysFont("comicsans", 40)

class Grid:

    def __init__(self, board, width, height):
        self.board = board
        self.rows = 9
        self.cols = 9
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(9)] for i in range(9)]
        self.width = width
        self.height = height
        self.model = None
        self.selected = None

    def draw(self, win):
        self.update_cubes()
        # Draw Grid Lines
        gap = self.width / 9
        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(win, (0, 0, 0), (0, i * gap), (self.width, i * gap), thick)
            pygame.draw.line(win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)

        # Draw Cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(win)

        draw_solve(win)

    def update_cubes(self):
        self.cubes = [[Cube(self.board[i][j], i, j, self.width, self.height) for j in range(9)] for i in range(9)]

    def solve(self):
        solve_res = solver.start_matrix_solve(self.board)
        solved_board = solve_res[0]
        solved = solve_res[1]
        solver.print_matrix(solved_board)
        print("solved: " + str(solved))
        solver.print_matrix(self.board)
        self.board = solved_board
        solver.print_matrix(self.board)
        self.update_cubes()

    def animated_solve(self, c, r):
        #print("started smth")
        #print(self.board)
        redraw_window(win, self)
        pygame.display.update()
#        time.sleep(0.001)
        if self.board[r][c] == 9:
            self.board[r][c] = 0
            return False

        self.board[r][c] += 1
        if solver.check_new_entry(self.board, self.board[r][c], c, r):
            (i, j) = solver.find_empty(self.board)
            if (i, j) == (9, 9) or self.animated_solve( j, i):
                return True
            else:
                return self.animated_solve( c, r)
        else:
            return self.animated_solve( c, r)

def draw_solve(surf):
    text = fnt.render("solve", True, (0,0,0))
    textRect = text.get_rect()
    textRect.center = (225,590)
    surf.blit(text, textRect)
    #surf.blit(text, (225, 590))

    pygame.draw.line(surf, (0, 0, 0), (125, 570), (425, 570), 4)
    pygame.draw.line(surf, (0, 0, 0), (125, 670), (425, 670), 4)
    pygame.draw.line(surf, (0, 0, 0), (125, 570), (125, 670), 4)
    pygame.draw.line(surf, (0, 0, 0), (425, 570), (425, 670), 4)


class Cube:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, win):

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), 1, (128, 128, 128))
            win.blit(text, (x + 5, y + 5))
        elif not (self.value == 0):
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))

        if self.selected:
            pygame.draw.rect(win, (255, 0, 0), (x, y, gap, gap), 3)

    def set(self, val):
        self.value = val

    def set_temp(self, val):
        self.temp = val


def redraw_window(win, board):
    win.fill((255, 255, 255))
    # Draw grid and board
    board.draw(win)


def clicked_solve(pos: tuple):
    # (125, 570, 300, 100)
    x = pos[0]
    y = pos[1]
    return 125 <= x <= 425 and 570 <= y <= 670


class Process(multiprocessing.Process):
    def __init__(self, board, proc_id):
        super(Process, self).__init__()
        self.id = proc_id
        self.board = board

    def run(self):
        if self.id == 0:
            redraw_window(win, self.board)
            pygame.display.update()
        if self.id == 1:
            print("starting the board solve")
            self.board.solve()

def run_GUI():
    pygame.display.set_caption("Sudoku")
    matrix = test_boards.T_1
    board = Grid(matrix, 540, 540)
    solved = False
    started_solve = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if clicked_solve(pos) and not started_solve:
                    board.animated_solve(0,0)
                    started_solve = True
        #redraw_window(win, board)
        #pygame.display.update()

run_GUI()
pygame.quit()
