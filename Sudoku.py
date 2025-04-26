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
        filled = 0
        max_attempts = 100  # Éviter les boucles infinies
        attempts = 0
        
        while filled < n and attempts < max_attempts:
            row, col = random.randint(0, 8), random.randint(0, 8)
            if self.board[row][col] != 0:
                attempts += 1
                continue
                
            # Trouver les nombres valides pour cette cellule
            valid_nums = [num for num in range(1, 10) if self.is_valid(row, col, num)]
            if valid_nums:
                self.board[row][col] = random.choice(valid_nums)
                filled += 1
            else:
                attempts += 1
        
        # Si on n'a pas pu remplir toutes les cellules, réinitialiser et réessayer
        if filled < n:
            self.board = [[0 for _ in range(9)] for _ in range(9)]
            self.fill_random_cells(n)

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
        # Trouver la cellule avec le moins de possibilités (heuristique MRV)
        empty = self.find_best_empty()
        if not empty:
            return True
        
        row, col = empty
        possible_values = self.get_possible_values(row, col)
        
        for num in possible_values:
            self.board[row][col] = num
            
            if self.solve_sudoku():
                return True
                
            self.board[row][col] = 0
            
        return False
    
    def find_best_empty(self):
        min_options = 10
        best_cell = None
        
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    options = self.count_valid_options(i, j)
                    if options < min_options:
                        min_options = options
                        best_cell = (i, j)
                        if min_options == 1:  # Optimisation : si une seule option, c'est forcément la meilleure
                            return best_cell
        
        return best_cell
    
    def count_valid_options(self, row, col):
        count = 0
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                count += 1
        return count
    
    def get_possible_values(self, row, col):
        return [num for num in range(1, 10) if self.is_valid(row, col, num)]

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def remove_numbers_based_on_difficulty(self):
        # Définir des plages de difficulté plus précises
        difficulty_ranges = {
            'easy': (35, 40),
            'medium': (45, 50),
            'hard': (55, 60)
        }
        
        min_cells, max_cells = difficulty_ranges.get(self.difficulty, (45, 50))
        cells_to_remove = random.randint(min_cells, max_cells)
        
        # Créer une liste de toutes les cellules remplies
        filled_cells = [(i, j) for i in range(9) for j in range(9) if self.board[i][j] != 0]
        random.shuffle(filled_cells)
        
        # Retirer les cellules une par une et vérifier l'unicité de la solution
        for row, col in filled_cells[:cells_to_remove]:
            temp = self.board[row][col]
            self.board[row][col] = 0
            
            # Pour les puzzles difficiles, vérifier que la solution reste unique
            if self.difficulty == 'hard' and not self.has_unique_solution():
                self.board[row][col] = temp  # Remettre le chiffre si la solution n'est plus unique
    
    def has_unique_solution(self):
        # Simplification - en production, il faudrait implémenter un vrai vérificateur d'unicité
        # en comptant le nombre de solutions possibles
        test_board = [row[:] for row in self.board]
        solver = Solver(test_board)
        return solver.count_solutions() == 1

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

    def check_solution(self, solution_board):
        """Vérifie si une solution proposée est correcte"""
        # Vérifier chaque ligne
        for row in solution_board:
            if sorted(row) != list(range(1, 10)):
                return False
                
        # Vérifier chaque colonne
        for col in range(9):
            if sorted([solution_board[row][col] for row in range(9)]) != list(range(1, 10)):
                return False
                
        # Vérifier chaque bloc 3x3
        for block_row in range(3):
            for block_col in range(3):
                block = []
                for i in range(3):
                    for j in range(3):
                        block.append(solution_board[block_row*3 + i][block_col*3 + j])
                if sorted(block) != list(range(1, 10)):
                    return False
                    
        return True

    def to_text(self):
        """Convertit la grille en format texte lisible"""
        result = []
        for i in range(9):
            if i % 3 == 0 and i != 0:
                result.append("------+-------+------")
            
            row = []
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    row.append("|")
                
                cell = str(self.board[i][j]) if self.board[i][j] != 0 else "."
                row.append(cell)
            
            result.append(" ".join(row))
        
        return "\n".join(result)


