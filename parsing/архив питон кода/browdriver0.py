from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from time import sleep
s=Service("c:\chromedriver.exe")            #так надо набирать, чтобы не было ошибки пути
browser = webdriver.Chrome(service=s)       #
browser.set_window_size(1600,900)           #надо изменить размер окна, чтобы прогрузились нужные элементы
url = "https://ru.bidspirit.com/ui/search/PAST.high_price.books_all.all."
browser.get(url)
sleep(10)
element = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div[10]/div/a[16]")
element.click()
