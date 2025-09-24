board = [[0 for _ in range(8)] for _ in range(8)]

def print_board(board):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))
    print()
    
    
def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
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
        return count["solutions"]

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_n_queens(board, col + 1, count)
            board[i][col] = 0

    return count["solutions"]

solution_count = solve_n_queens(board, 0)
print(f"Total number of solutions: {solution_count}")