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
