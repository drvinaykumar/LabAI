import random

def is_consistent(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def ac3(board, row, n):
    # Check arc consistency for the current queen
    for i in range(row):
        if board[i] == board[row]:
            return False
        if abs(board[i] - board[row]) == abs(i - row):
            return False
    return True

def min_conflicts(board, n, max_iter):
    for _ in range(max_iter):
        conflicts = []
        for col in range(n):
            conflicts_count = 0
            for row in range(n):
                if row != col and board[row] == col:
                    conflicts_count += 1
                if abs(row - col) == abs(board[row] - col):
                    conflicts_count += 1
            conflicts.append(conflicts_count)

        max_conflicts = max(conflicts)
        max_conflict_cols = [i for i, count in enumerate(conflicts) if count == max_conflicts]
        col_to_change = random.choice(max_conflict_cols)
        board[col_to_change] = min(range(n), key=lambda row: conflicts[row])
        
        if max_conflicts == 0:
            return board

    raise Exception("No solution found in the given number of iterations")

def solve_nqueens(n, max_iter=1000):
    board = [-1] * n  # Initialize the board with no queens placed
    for row in range(n):
        if ac3(board, row, n):
            continue
        else:
            for col in range(n):
                if is_consistent(board, row, col):
                    board[row] = col
                    break

    if -1 not in board:
        return board  # A solution is found using AC-3

    return min_conflicts(board, n, max_iter)  # Use Minimum Conflict algorithm to resolve remaining conflicts

def print_board(board):
    for row in board:
        line = ['.'] * len(board)
        line[row] = 'Q'
        print(" ".join(line))

if __name__ == "__main__":
    n = 8  # Change the board size as needed
    solution = solve_nqueens(n)
    if solution:
        print_board(solution)
    else:
        print("No solution found.")
