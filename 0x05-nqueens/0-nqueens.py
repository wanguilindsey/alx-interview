#!/usr/bin/python3
"""
Solves the N-Queens problem.
"""
import sys


def backtrack(r, n, cols, pos, neg, board):
    """
    Recursively places queens on the board and prints solutions.
    """
    if r == n:
        res = []
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 1:
                    res.append([row, col])
        print(res)
        return

    for c in range(n):
        if c in cols or (r + c) in pos or (r - c) in neg:
            continue

        cols.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board[r][c] = 1

        backtrack(r + 1, n, cols, pos, neg, board)

        cols.remove(c)
        pos.remove(r + c)
        neg.remove(r - c)
        board[r][c] = 0


def nqueens(n):
    """
    Solves N-Queens for a given board size n.
    Args:
        n (int): Size of the board (number of queens).
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for i in range(n)]

    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nn = int(n[1])
        if nn < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(nn)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
