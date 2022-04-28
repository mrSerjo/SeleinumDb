import os
import sqlite3
from selenium import webdriver

from selenium.webdriver.common.by import By


conn = sqlite3.connect('FNS-MSP-2019-sg2.sqlite3', check_same_thread=False)

inn_list = []
director_list = []
error_inns = []  # если гендир не найден, сюда добалвяется инн

cursor = conn.cursor()
cursor.execute("""
    SELECT * FROM dohrash
    ORDER BY СумДоход
    LIMIT 25;
""")
records = cursor.fetchall()
for row in records:
     inn_list.append(row[1])

cursor.close()
print(inn_list)


url = 'https://www.rusprofile.ru/'

inn_check_error_text = "гендир не найден"

driver_path = os.path.abspath(os.curdir + '/chromedriver/chromedriver.exe')


def run_check(inn):
     try:
          driver = webdriver.Chrome(executable_path=driver_path)
          driver.get(url=url)

          inn_imput = driver.find_element(by=By.NAME, value='query')
          inn_imput.clear()
          inn_imput.send_keys(inn_list[i])
          my_click = driver.find_element(By.CSS_SELECTOR, '[class = "search-btn waves-effect waves-light"]').click()

          gen_dir = driver.find_element(By.CSS_SELECTOR, '[data-goal-param = "interactions, person_ul"]')
          # director_list.append(gen_dir.text)
          return gen_dir.text

     except Exception as ex:
          print(ex)
          return inn_check_error_text
     finally:
          driver.close()
          driver.quit()


for i in range(len(inn_list)):
     result = run_check(inn_list[i])
     if not result == inn_check_error_text:
          director_list.append(result)
     else:
          error_inns.append(inn_list[i])


print(director_list)