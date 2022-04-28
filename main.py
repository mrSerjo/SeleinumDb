from bs4 import BeautifulSoup
import requests
import sqlite3
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


conn = sqlite3.connect('FNS-MSP-2019-sg2.sqlite3', check_same_thread=False)

inn_list = []
director_list = []

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

driver = webdriver.Chrome(executable_path=r'D:\Dev\SeleinumDb\chromedriver\chromedriver.exe')


url = 'https://www.rusprofile.ru/'

try:
     driver.get(url=url)

     inn_imput = driver.find_element(by=By.NAME, value='query')
     inn_imput.clear()
     inn_imput.send_keys('5321186807')
     my_click = driver.find_element(By.CSS_SELECTOR, '[class = "search-btn waves-effect waves-light"]').click()

     gen_dir = driver.find_element(By.CSS_SELECTOR, '[data-goal-param = "interactions, person_ul"]')
     print(gen_dir.text)

except Exception as ex:
     print(ex)
finally:
     driver.close()
     driver.quit()

# res = requests.get(url)
#
# soup = BeautifulSoup(res.text, 'lxml')
# print(soup)

