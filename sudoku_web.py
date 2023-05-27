from selenium import webdriver
from bs4 import BeautifulSoup
import solve_sudoku
import time

driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.maximize_window()
driver.get('http://sudoku99.co.kr/')
# driver.get('http://sudoku99.co.kr/sudoku9x9/20_level_17_hint/')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


sudoku_matrix = []

for i in range(1, 10):
    sudoku_row = []
    for j in range(1, 10):
        sudoku_num = soup.select(f'#q{i}{j}')[0].get('value')
        print(sudoku_num)
        if sudoku_num == '':
            sudoku_num = '0'
        sudoku_row.append(int(sudoku_num))
    sudoku_matrix.append(sudoku_row)

solve_sudoku.solve_sudoku(sudoku_matrix)

print(sudoku_matrix)

# time.sleep(5)

for i in range(1, 10):
    for j in range(1, 10):
        # time.sleep(1)

        space = soup.select(f'#q{i}{j}')[0].get('value')
        if space != '':
            continue

        driver.find_element(by='xpath', value=f'//*[@id="q{i}{j}"]').send_keys(str(sudoku_matrix[i - 1][j - 1]))
