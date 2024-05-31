# sudoku_solver.py

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def parse_input():
    board = []
    print("请输入数独谜题，每行9个字符，空位用 '-' 表示:")
    for i in range(9):
        while True:
            line = input(f"第 {i + 1} 行: ")
            if len(line) == 9 and all(c in '123456789-' for c in line):
                board.append([int(c) if c != '-' else 0 for c in line])
                break
            else:
                print("输入不合法，请重新输入。")
    return board

if __name__ == "__main__":
    board = parse_input()

    if solve_sudoku(board):
        print("Sudoku solved successfully:")
        print_board(board)
    else:
        print("No solution exists")
