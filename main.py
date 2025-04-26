# Author: Jalal Azouzout
# Date: 25/07/2021
# Description: A simple Sudoku api with a random board generator
# Version: 1.0

from Sudoku import Sudoku
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/sudoku', methods=['GET'])
def generate_sudoku():
    try:
        difficulty = request.args.get('difficulty', 'medium')
        if difficulty not in ['easy', 'medium', 'hard']:
            return jsonify({'error': 'Invalid difficulty level'}), 400
            
        sudoku = Sudoku(difficulty)
        return jsonify({'difficulty': difficulty, 'board': sudoku.board, 'solved_board': sudoku.solved_sudoku})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)


