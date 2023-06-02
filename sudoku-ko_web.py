from selenium import webdriver
from bs4 import BeautifulSoup
import solve_sudoku
import time

driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.maximize_window()
driver.get('https://sudoku-ko.com/')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


sudoku_matrix = []

for i in range(0, 9):
    sudoku_row = []
    for j in range(0, 9):
        sudoku_num = soup.select(f'#c_{j}_{i}')[0].get_text()
        # print(sudoku_num)
        if sudoku_num == ' ':
            sudoku_num = '0'
        sudoku_row.append(int(sudoku_num))
    sudoku_matrix.append(sudoku_row)

solve_sudoku.solve_sudoku(sudoku_matrix)

print(sudoku_matrix)

# time.sleep(5)
driver.find_element(by='xpath', value='//*[@id="rv"]').click()

for i in range(9):
    for j in range(9):
        # time.sleep(1)

        space = soup.select(f'#c_{j}_{i}')[0].get_text()
        if space != ' ':
            continue

        driver.find_element(by='xpath', value=f'//*[@id="vc_{j}_{i}"]').click()
        time.sleep(1)
        driver.find_element(by='xpath', value=f'//*[@id="ot{sudoku_matrix[i][j]}"]').click()
        time.sleep(1)
        # sudoku_matrix[i][j]
