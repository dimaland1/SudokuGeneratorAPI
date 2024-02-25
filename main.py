# Author: Jalal Azouzout
# Date: 25/07/2021
# Description: A simple Sudoku api with a random board generator
# Version: 1.0

from Sudoku import Sudoku
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sudoku', methods=['GET'])
def generate_sudoku():
    
    difficulty = request.args.get('difficulty', 'medium')
    sudoku = Sudoku(difficulty)
    
    return jsonify({'difficulty' : difficulty,'board': sudoku.board, 'solved_board': sudoku.solved_sudoku})

if __name__ == "__main__":
    app.run(debug=True)


