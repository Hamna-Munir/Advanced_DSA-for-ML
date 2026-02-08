"""
backtracking_nqueens.py
Solve N-Queens problem using backtracking.
"""

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_nqueens(board, row, n, solutions):
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(board, row+1, n, solutions)

if __name__ == "__main__":
    n = 4
    solutions = []
    solve_nqueens([0]*n, 0, n, solutions)
    print(f"All solutions for {n}-Queens:")
    for sol in solutions:
        print(sol)

# Output:
# All solutions for 4-Queens:
# [1, 3, 0, 2]
# [2, 0, 3, 1]
