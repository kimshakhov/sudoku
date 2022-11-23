import pygame
import solver


class Grid:

    def __init__(self, board, width, height):
        self.board = board
        self.rows = 9
        self.cols = 9
        self.cubes = [[Cube(self.board[i][j], i, j, width, height) for j in range(9)] for i in range(9)]
        self.width = width
        self.height = height

    def draw(self, surf, fnt):
        self.update_cubes()
        gap = self.width / 9
        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(surf, (0, 0, 0), (0, i * gap), (self.width, i * gap), thick)
            pygame.draw.line(surf, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)

        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(surf, fnt)

        draw_solve(surf, fnt)

    def update_cubes(self):
        self.cubes = [[Cube(self.board[i][j], i, j, self.width, self.height) for j in range(9)] for i in range(9)]

    def solve(self):
        solve_res = solver.start_matrix_solve(self.board)
        solver.print_matrix(self.board)
        self.update_cubes()

    def animated_solve(self, c, r, surf, fnt):
        redraw_window(surf, fnt, self)
        pygame.display.update()
        if self.board[r][c] == 9:
            self.board[r][c] = 0
            return False

        self.board[r][c] += 1
        if solver.check_new_entry(self.board, self.board[r][c], c, r):
            (i, j) = solver.find_empty(self.board)
            if (i, j) == (9, 9) or self.animated_solve(j, i, surf, fnt):
                return True
            else:
                return self.animated_solve(c, r, surf, fnt)
        else:
            return self.animated_solve(c, r, surf, fnt)


def draw_solve(surf, fnt):
    text = fnt.render("space to", True, (0, 0, 0))
    text2 = fnt.render("solve", True, (0, 0, 0))
    surf.blit(text, (30, 550))
    surf.blit(text2, (30, 590))


class Cube:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def draw(self, surf, fnt):
        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        if not (self.value == 0):
            text = fnt.render(str(self.value), 1, (0, 0, 0))
            surf.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))


def redraw_window(surf, fnt, board):
    surf.fill((255, 255, 255))
    board.draw(surf, fnt)


def run_GUI(matrix):
    pygame.font.init()
    surf = pygame.display.set_mode((550, 700))
    fnt = pygame.font.SysFont("comicsans", 40, False, True)
    pygame.display.set_caption("Sudoku")
    board = Grid(matrix, 540, 540)
    run = True
    started_solve = False

    while run:
        redraw_window(surf, fnt, board)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started_solve:
                    start = solver.find_empty(board.board)
                    board.animated_solve(start[0], start[1], surf, fnt)
                    started_solve = True
                if event.key == pygame.K_q:
                    run = False

    pygame.quit()
