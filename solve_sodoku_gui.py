import tkinter as tk
from tkinter import messagebox
import random
import solve_sudoku

class Auto_ApplicateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SUDOKU")
        self.create_entry_widget()
        # self.root.geometry("870x800")


    # 테스트 스도쿠 만들기
    def generate_testsudoku(self):
        self.clear()
        sudoku = [[0] * 9 for _ in range(9)]
        sudoku_local = [(i, j) for i in range(9) for j in range(9)]

        # 랜덤하게 엔트리창 20개 뽑기
        random_sudoku_local_list = random.sample(sudoku_local, 20)

        for row, col in random_sudoku_local_list:
            num = random.randint(1, 9)
            if solve_sudoku.is_valid(sudoku, row, col, num):
                sudoku[row][col] = num
                self.entries[(row, col)].insert(tk.END, str(num))


    # 엔트리창 모두 치우기
    def clear(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)



    # 스도쿠 풀기 함수
    def validate(self):
        def print_sudoku(sudoku):
            for row in sudoku:
                print(" ".join(str(num) for num in row))
        sudoku = [[0] * 9 for _ in range(9)]
        for index, entry in self.entries.items():
            try:
                if entry.get() != "":
                    sudoku[index[0]][index[1]] = int(entry.get())
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter only numbers.")
                return
        if not solve_sudoku.solve_sudoku(sudoku):
            messagebox.showerror("Error", "This puzzle can't be solved.")


        else:
            for index, entry in self.entries.items():
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(sudoku[index[0]][index[1]]))

    # 엔트리창에 숫자 입력시 규칙에 맞는지 안맞으면 엔트리창 숫자 색깔 변경하기
    def show_entry_valid(self, event):
        # 엔트리 폰트색상 검정색으로 다시 바꾸기
        for index, entry in self.entries.items():
            entry.config(fg='black')
        # 스도쿠리스트 만들기
        sudoku = [[0] * 9 for _ in range(9)]
        for index, entry in self.entries.items():
            try:
                if entry.get() != "":
                    sudoku[index[0]][index[1]] = int(entry.get())
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter only numbers.")
                return

        for index, entry in self.entries.items():
            try:
                num = int(entry.get())
            except:
                continue


            # 가로축에서 조회하기
            for x in range(9):
                if x == index[1]:
                    continue
                if sudoku[index[0]][x] == num:
                    entry.config(fg='red')
            # 세로축에서 조회하기
            for y in range(9):
                if y == index[0]:
                    continue
                if sudoku[y][index[1]] == num:
                    entry.config(fg='red')

            start_row, start_col = 3 * (index[0] // 3), 3 * (index[1] // 3)
            for i in range(3):
                for j in range(3):
                    if i + start_row == index[0] and j + start_col == index[1]:
                        continue
                    if sudoku[i + start_row][j + start_col] == num:
                        entry.config(fg='red')




    def create_entry_widget(self):
        self.entries = {}
        for i in range(3):
            for j in range(3):
                self.frame = tk.Frame(self.root, borderwidth=1, relief='solid')
                self.frame.grid(row=i, column=j, padx=0, pady=0)

                # 각 프레임 내부에 가로세로 3x3 그리드로 Entry 위젯을 배치합니다.
                for x in range(3):
                    for y in range(3):
                        self.entries[((i*3)+x, (j*3)+y)] = tk.Entry(self.frame, width=2, font=('Arial', 20), justify='center')
                        self.entries[((i*3)+x, (j*3)+y)].grid(row=x, column=y)
                        self.entries[((i * 3) + x, (j * 3) + y)].bind('<KeyRelease>', self.show_entry_valid)


        solve_button = tk.Button(self.root, text="Solve", command=self.validate)
        solve_button.grid(row=9, column=0)
        clear_button = tk.Button(self.root, text="Clear", command=self.clear)
        clear_button.grid(row=9, column=1)
        test_button = tk.Button(self.root, text="Test", command=self.generate_testsudoku)
        test_button.grid(row=9, column=2)



if __name__ == "__main__":
    root = tk.Tk()
    app = Auto_ApplicateApp(root)
    root.mainloop()
