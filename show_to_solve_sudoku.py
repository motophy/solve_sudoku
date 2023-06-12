import matplotlib.pyplot as plt
import numpy as np
import time

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
            draw_sudoku(sudoku, row, col)  # Draw each step
            # time.sleep(0.001)  # Add delay
            if solve_sudoku(sudoku, row, col + 1):
                return True
    sudoku[row][col] = 0
    return False

def draw_sudoku(sudoku, row=-1, col=-1):
    # Clear the previous figure
    plt.clf()

    # Draw the grid
    for x in range(10):
        if x % 3 == 0:
            plt.plot([x, x], [0, 9], 'k', linewidth=2)
            plt.plot([0, 9], [x, x], 'k', linewidth=2)
        else:
            plt.plot([x, x], [0, 9], 'k')
            plt.plot([0, 9], [x, x], 'k')

    # Draw the numbers
    for x in range(9):
        for y in range(9):
            if sudoku[y][x] != 0:
                if (x == col and y == row):
                    plt.text(x + 0.5, 9 - y - 0.5, str(sudoku[y][x]),
                             fontsize=20, ha='center', va='center', color='red')
                else:
                    plt.text(x + 0.5, 9 - y - 0.5, str(sudoku[y][x]),
                             fontsize=20, ha='center', va='center')

    # Show the plot
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

if __name__ == "__main__":
    draw_sudoku(example_sudoku)
    if solve_sudoku(example_sudoku):
        draw_sudoku(example_sudoku)
    else:
        print("No solution exists.")
