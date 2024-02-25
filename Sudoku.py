# Author: Jalal Azouzout
# Date: 25/07/2021
# Description: A simple Sudoku game with a random board generator
# Version: 1.0

import random

class Sudoku:
    def __init__(self, difficulty='medium'):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.difficulty = difficulty
        self.fill_random_cells()
        self.solve_sudoku()
        self.solved_sudoku = [row[:] for row in self.board]
        self.remove_numbers_based_on_difficulty()

    def fill_random_cells(self, n=10):
        for _ in range(n):
            row, col = random.randint(0, 8), random.randint(0, 8)
            num = random.randint(1, 9)
            while not self.is_valid(row, col, num) or self.board[row][col] != 0:
                row, col = random.randint(0, 8), random.randint(0, 8)
                num = random.randint(1, 9)
            self.board[row][col] = num

    def is_valid(self, row, col, num):
        for x in range(9):
            if self.board[row][x] == num or self.board[x][col] == num:
                return False

        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.board[i + startRow][j + startCol] == num:
                    return False

        return True

    def solve_sudoku(self):
        empty = self.find_empty()
        if not empty:
            return True
        row, col = empty

        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row][col] = num

                if self.solve_sudoku():
                    return True

                self.board[row][col] = 0

        return False

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def remove_numbers_based_on_difficulty(self):
        attempts = {
            'easy': 40,
            'medium': 45,
            'hard': 50
        }.get(self.difficulty, 45)  # Default to medium if invalid difficulty

        cells_removed = 0
        while cells_removed < attempts:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                cells_removed += 1

    def print_board(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - -")

            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")


