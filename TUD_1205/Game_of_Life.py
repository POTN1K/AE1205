# Assignment Five. A cellular automation simulation "Game of Life"
# Author: Nikolaus Ricker

# ------------------------------------------------------
# Libraries
import numpy as np
import pygame as pg


# ------------------------------------------------------
# Functions
def SumCells(cell, x, y):
    """Adds the number of living cells surrounding"""
    sum_ = 0
    check = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y),
             (x + 1, y + 1)]
    shape = cell.shape

    for pos in check:
        if 0 <= pos[0] < shape[0] and 0 <= pos[1] < shape[1]:
            if cell[pos[0], pos[1]] == 1:
                sum_ += 1
    return sum_


def UpdateCells(cells_in):
    """Takes the original cell board and returns an updated cell board"""
    cells_out = np.zeros_like(cells_in)
    i, j = cells_in.shape
    for row in range(i):
        for col in range(j):
            alive = SumCells(cells_in, row, col)
            if cells_in[row, col] == 1:
                if 2 <= alive <= 3:
                    cells_out[row, col] = 1
            elif cells_in[row, col] == 0:
                if alive == 3:
                    cells_out[row, col] = 1
    return cells_out


def DrawGrid(n_, length_):
    """Creates a grid for the game"""
    block = int(length_ / n_)
    for x in range(0, length_, block):
        for y in range(0, length_, block):
            rect = pg.Rect(x, y, block, block)
            pg.draw.rect(scr, (0, 0, 0), rect, 1)


def VSumCells(cell):
    """Sums neighbours by vectorization, moving it around"""
    cell_ = np.pad(cell, ((1, 1), (1, 1)), constant_values=0)
    sum = np.roll(cell_, 1, axis=1) + np.roll(cell_, -1, axis=1) + +np.roll(cell_, 1, axis=0) + \
          np.roll(cell_, -1, axis=0) + np.roll(cell_, (1, 1), axis=(0, 1)) + np.roll(cell_, (-1, -1), axis=(0, 1)) + \
          np.roll(cell_, (-1, 1), axis=(0, 1)) + np.roll(cell_, (1, -1), axis=(0, 1))
    return sum, cell_


def VUpdateCells(in_cell):
    """Updates cells base on number of surrounding neighbours"""
    sum_, cell_ = VSumCells(in_cell)
    cells_out = np.where(np.logical_or(sum_ == 3, np.logical_and(sum_ == 2, cell_ == 1)), 1, 0)
    m, n = sum_.shape
    cells_out = np.delete(cells_out, (0, m - 1), 0)
    cells_out = np.delete(cells_out, (0, n - 1), 1)
    return cells_out


def Read106(file):
    """Reads the file and append it to a table"""
    table = []
    table2 = []
    with open(file) as dat:
        dat.readline()
        for line in dat.readlines():
            table.append(line.strip('\n').split())

    for i in table:
        temp = []
        for ind, item in enumerate(i):
            j = int(item)
            temp.append(j)
        table2.append(temp)
    return table2


def InsertPattern(board_, table=[]):
    if not table:
        board_[1:4, 1:4] = [[0, 1, 0],
                            [0, 0, 1],
                            [1, 1, 1]]
    else:
        m, n = board_.shape
        x_center = int(m / 2)
        y_center = int(n / 2)
        for value in table:
            x = x_center + value[0]
            y = y_center + value[1]
            board_[x, y] = 1
    return board_


# ------------------------------------------------------
# Program
# Fill values
size = 50
pos = input("Which file do you want to see? (1,2,3)")
file1 = './Data/Game_of_Life/ak47reaction_106.lif'
file2 = './Data/Game_of_Life/b52bomber_106.lif'
file3 = './Data/Game_of_Life/barge2spaceship_106.lif'

# Initializing board
board = np.zeros((size, size))
# Setting initial positions
if pos == '1':
    positions = Read106(file1)
    board = InsertPattern(board, positions)
if pos == '2':
    positions = Read106(file1)
    board = InsertPattern(board, positions)
if pos == '3':
    positions = Read106(file1)
    board = InsertPattern(board, positions)
else:
    board = InsertPattern(board)

# ------------------------------------------------------
# Pygame
# Set initial configuration
pg.init()
pg.display.set_caption("Game of Life")

length = size * 15
reso = (length, length)
scr = pg.display.set_mode(reso)
scrrect = scr.get_rect()

alive = (0, 128, 0)
background = (255, 255, 255)
scr.fill(background)
block = length / size

# Run simulation
running = True
while running:
    # Close simulation
    pg.event.pump()
    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        running = False
    # Draw
    scr.fill(background)
    DrawGrid(size, length)
    i, j = board.shape
    for row in range(i):
        for col in range(j):
            if board[row][col] == 1:
                x = int(row / size * length)
                y = length - int(col / size * length)
                cell = pg.Rect(x, y, block, block)
                pg.draw.rect(scr, alive, cell)
    board = VUpdateCells(board)
    pg.time.delay(100)
    pg.display.flip()
pg.quit()
