N = 4


def print_board(board):
    for row in board:
        print(row)
    print()


def is_safe(board, row, col):
    # Check left side of row
    for c in range(col):
        if board[row][c] == 1:
            return False

    # Check upper-left diagonal
    r, c = row, col
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1

    # Check lower-left diagonal
    r, c = row, col
    while r < N and c >= 0:
        if board[r][c] == 1:
            return False
        r += 1
        c -= 1

    return True


def solve(col, board):
    if col == N:
        print_board(board)
        return True

    for row in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1

            if solve(col + 1, board):
                return True

            board[row][col] = 0  # backtrack

    return False


board = [[0] * N for _ in range(N)]
solve(0, board)
