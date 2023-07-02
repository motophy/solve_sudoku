import matplotlib.pyplot as plt
import numpy as np
import time

# 스도쿠 규칙에 맞는지 검사하는 함수
def is_valid(sudoku, row, col, num):
    # 행과 열에 동일한 숫자가 있는지 검사
    for i in range(9):
        if sudoku[row][i] == num or sudoku[i][col] == num:
            return False

    # 3x3 박스에 동일한 숫자가 있는지 검사
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if sudoku[i + start_row][j + start_col] == num:
                return False

    # 위의 조건들을 모두 만족하면 숫자를 배치할 수 있음
    return True


# 스도쿠를 해결하는 함수
def solve_sudoku(sudoku, row=0, col=0):
    # 현재 행의 마지막에 도달한 경우 다음 행으로 이동
    if col == 9:
        if row == 8:  # 마지막 행까지 확인한 경우 스도쿠가 완성된 것으로 판단
            return True
        row += 1
        col = 0

    # 빈 칸이 아닌 경우 다음 칸으로 이동
    if sudoku[row][col] != 0:
        return solve_sudoku(sudoku, row, col + 1)

    # 1부터 9까지의 숫자를 시도
    for num in range(1, 10):
        # 해당 숫자를 현재 위치에 배치할 수 있는지 확인
        if is_valid(sudoku, row, col, num):
            sudoku[row][col] = num
            if solve_sudoku(sudoku, row, col + 1):  # 다음 칸으로 이동
                return True

    # 위의 조건들을 만족하는 숫자를 찾지 못한 경우 백트래킹 수행
    sudoku[row][col] = 0
    return False


# 스도쿠 그리드를 그리는 함수
def draw_sudoku(sudoku, row=-1, col=-1):
    # 이전에 그려진 그림을 지움
    plt.clf()

    # 9x9 그리드를 그림
    for x in range(10):
        if x % 3 == 0:
            plt.plot([x, x], [0, 9], 'k', linewidth=2)
            plt.plot([0, 9], [x, x], 'k', linewidth=2)
        else:
            plt.plot([x, x], [0, 9], 'k')
            plt.plot([0, 9], [x, x], 'k')

    # 각 셀에 숫자를 씀
    for x in range(9):
        for y in range(9):
            if sudoku[y][x] != 0:
                if (x == col and y == row):  # 현재 위치를 빨간색으로 표시
                    plt.text(x + 0.5, 9 - y - 0.5, str(sudoku[y][x]),
                             fontsize=20, ha='center', va='center', color='red')
                else:
                    plt.text(x + 0.5, 9 - y - 0.5, str(sudoku[y][x]),
                             fontsize=20, ha='center', va='center')

    # 그림을 출력
    plt.axis('off')
    plt.grid(False)
    plt.show(block=False)
    plt.pause(0.1)

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

# 스도쿠 문제와 해결 과정을 실행하는 메인 함수
if __name__ == "__main__":
    draw_sudoku(example_sudoku)  # 스도쿠 초기 상태 그리기
    if solve_sudoku(example_sudoku):  # 스도쿠 풀이 시작
        draw_sudoku(example_sudoku)  # 해결된 스도쿠 그리기
    else:
        print("No solution exists.")  # 해결할 수 없는 스도쿠인 경우 메시지 출력
