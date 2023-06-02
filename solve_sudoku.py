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
    # 순서대로 칸 이동하기
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0
    # 빈칸이 아닐경우 넘기기(빈칸은 0으로)
    if sudoku[row][col] != 0:
        return solve_sudoku(sudoku, row, col + 1)
    for num in range(1, 10):
        # 순차적으로 숫자 대입하여 확인하기
        if is_valid(sudoku, row, col, num):
            # true 반환시 해당 숫자 스도쿠에 입력
            sudoku[row][col] = num
            # 다음칸으로 넘어가기
            if solve_sudoku(sudoku, row, col + 1):
                return True
    # 1~9까지 숫자대입에 실패하였을경우 False 반환하고 빈칸 0을 다시 넣고 이전 칸으로 재귀
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