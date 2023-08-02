#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True

def nqueens(N, row=0, board=None, solutions=[]):
    if board is None:
        board = [[0 for _ in range(N)] for _ in range(N)]

    if row == N:
        solutions.append([[i, row] for i, row in enumerate(board)])
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            nqueens(N, row + 1, board, solutions)
            board[row][col] = 0

def print_solutions(N):
    solutions = []
    nqueens(N, 0, None, solutions)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    print_solutions(N)
