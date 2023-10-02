def solve_n_queens(n):
    def is_safe(board, row, col):
  
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def backtrack(row):
        nonlocal solutions
        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)

    solutions = []
    board = [-1] * n
    backtrack(0)
    return solutions

n = 4
solutions = solve_n_queens(n)
for solution in solutions:
    for row in solution:
        print(' '.join('Q' if i == row else '.' for i in range(n)))
    print()
