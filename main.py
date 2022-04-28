from bs4 import BeautifulSoup
import requests
import sqlite3


conn = sqlite3.connect('FNS-MSP-2019-sg2.sqlite3', check_same_thread=False)


res = requests.get('FNS-MSP-2019-sg2.sqlite3')
soup = BeautifulSoup()

