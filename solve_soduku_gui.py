import tkinter as tk
from tkinter import messagebox
import random

# 해당 위치에 숫자를 넣을 수 있는지 검사하는 함수
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

# 스도쿠를 푸는 함수
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

# 모든 입력 필드를 초기화하는 함수
def clear(entries):
    for entry in entries.values():
        entry.delete(0, tk.END)

# 임의의 스도쿠 문제를 생성하는 함수
def generate_sudoku(entries):
    clear(entries)
    sudoku = [[0]*9 for _ in range(9)]
    for _ in range(20): # 무작위 위치에 숫자 삽입 (20회 반복)
        row, col, num = random.randint(0, 8), random.randint(0, 8), random.randint(1, 9)
        if is_valid(sudoku, row, col, num):
            sudoku[row][col] = num
            entries[(col, row)].insert(tk.END, str(num))

# 스도쿠 보드의 값들을 검증하고 스도쿠를 푸는 함수
def validate(entries):
    sudoku = [[0]*9 for _ in range(9)]
    for index, entry in entries.items():
        try:
            if entry.get() != "":
                sudoku[index[1]][index[0]] = int(entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter only numbers.")
            return
    if not solve_sudoku(sudoku):
        messagebox.showerror("Error", "This puzzle can't be solved.")
    else:
        for index, entry in entries.items():
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(sudoku[index[1]][index[0]]))

def main():
    window = tk.Tk()
    window.title("Sudoku Solver")
    entries = {}
    for i in range(9):
        for j in range(9):
            entries[(i, j)] = tk.Entry(window, width=5, font=('Arial', 14))
            entries[(i, j)].grid(row=j, column=i, padx=1, pady=1)
            if (i % 3 == 2) and (i < 8):
                tk.Frame(window, width=2, bg="black").grid(row=j, column=i+1)
            if (j % 3 == 2) and (j < 8):
                tk.Frame(window, height=2, bg="black").grid(row=j+1, column=i, sticky='we')
    solve_button = tk.Button(window, text="Solve", command=lambda: validate(entries))
    solve_button.grid(row=9, column=0, columnspan=3)
    clear_button = tk.Button(window, text="Clear", command=lambda: clear(entries))
    clear_button.grid(row=9, column=3, columnspan=3)
    test_button = tk.Button(window, text="Test", command=lambda: generate_sudoku(entries))
    test_button.grid(row=9, column=6, columnspan=3)
    window.mainloop()

if __name__ == "__main__":
    main()
