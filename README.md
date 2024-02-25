# SudokuGenerator

## Project Overview

This project is a Flask-based API for generating and solving Sudoku puzzles. It allows users to generate Sudoku puzzles of varying difficulty (easy, medium, hard) via a simple API request. The puzzles are generated using a backtracking algorithm and can be solved using the same logic.

## Features

- Support for different difficulty levels: easy, medium, hard.
- Backtracking algorithm for generating and solving puzzles.

## Requirements

- Python 3.x
- Flask

## Installation

To install this project, clone the repository and install the required Python packages.

```bash
git clone https://github.com/dimaland1/SudokuGeneratorAPI.git
cd SudokuGeneratorAPI
pip install -r requirements.txt
```

## How It Works

The API uses the Sudoku class to generate a complete puzzle based on the specified difficulty. The GET /sudoku endpoint accepts a difficulty parameter and returns a Sudoku puzzle as a JSON response.


## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.
