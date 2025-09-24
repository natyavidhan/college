board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

def print_board(board):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))
    print()
    
    
def is_safe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col, count=None):
    if count is None:
        count = {"solutions": 0}
        
    if col >= len(board):
        print_board(board)
        count["solutions"] += 1
        return count["solutions"]  # Return the count, not True/False

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1  # Place queen

            # Recur to place the rest of the queens
            solve_n_queens(board, col + 1, count)

            board[i][col] = 0  # Backtrack

    return count["solutions"]

solution_count = solve_n_queens(board, 0)
print(f"Total number of solutions: {solution_count}")