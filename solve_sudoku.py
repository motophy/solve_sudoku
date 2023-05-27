def is_valid(sudoku, row, col, num):
    for i in range(9):
        if sudoku[row][i] == num or sudoku[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if sudoku[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(sudoku, row=0, col=0):
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    if sudoku[row][col] != 0:
        return solve_sudoku(sudoku, row, col + 1)
    for num in range(1, 10):
        if is_valid(sudoku, row, col, num):
            sudoku[row][col] = num
            if solve_sudoku(sudoku, row, col + 1):
                return True
    sudoku[row][col] = 0
    return False

def print_sudoku(sudoku):
    for row in sudoku:
        print(" ".join(str(num) for num in row))

example_sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if __name__ == "__main__":
    if solve_sudoku(example_sudoku):
        print_sudoku(example_sudoku)
    else:
        print("No solution exists.")