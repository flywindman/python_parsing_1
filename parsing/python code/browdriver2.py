from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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
sleep(40)                                       # нужна задержка, пока не прогрузится страница

for p in range(200):
    print(p)    
    soup = BeautifulSoup(browser.page_source, "lxml")
    books = soup.find_all("div", class_="item-link ng-isolate-scope")
    print(len(books))
    for item in books:
#        try:
#            lot_name = item.find("span", class_="lot-name").text.strip()
#        except Exception:
#            lot_name = "No data"
#
#        try:
#            lot_sold = item.find("div", class_="text").text.strip()
#        except Exception:
#            lot_sold = "No data"
#        try:
#            lot_cost = item.find("div", class_="lot-price-row ng-scope").text.strip()
#        except Exception:
#            lot_cost = "No data"
        try:
            lot_lincs = "https://ru.bidspirit.com" + item.find("a", class_="orange").get("href")
        except Exception:
            lot_lincs = "No data"
            
        #print(lot_name, " ", lot_sold, " ",lot_cost, " ", lot_lincs)
        with open("list.txt", "a") as file:
            try:
                            file.write(lot_lincs + '\n')
            except UnicodeEncodeError:
                            pass

    element = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div[10]/div/a[16]")
    element.click()
    sleep(7)
    
