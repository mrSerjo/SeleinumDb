from bs4 import BeautifulSoup
import requests
import sqlite3


conn = sqlite3.connect('FNS-MSP-2019-sg2.sqlite3', check_same_thread=False)

cursor = conn.cursor()
cursor.execute("""
    SELECT * FROM dohrash
    ORDER BY СумДоход
    LIMIT 25;
""")
records = cursor.fetchall()
for row in records:
    print('INN:', row[1])
print(records)

cursor.close()


# res = requests.get('FNS-MSP-2019-sg2.sqlite3')
# soup = BeautifulSoup()

