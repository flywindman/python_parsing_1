from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from time import sleep
s=Service("c:\chromedriver.exe")            #так надо набирать, чтобы не было ошибки пути
browser = webdriver.Chrome(service=s)       #
url = "https://ru.bidspirit.com/ui/catalog/auction/litfund/19913/1"
browser.get(url)
sleep(30)                                       # нужна задержка, пока не прогрузится страница
soup = BeautifulSoup(browser.page_source, "lxml")
books = soup.find_all("div", class_="item ng-scope ng-isolate-scope pc-item")
for item in books:
    lot_name = item.find("span", class_="lot-name").text
    print(lot_name)
    lot_namber = item.find("span", class_="lot-number").text
    lot_sold = item.find("div", class_="text").text
    lot_cost = item.find("div", class_="lot-price-row ng-scope").text
    lot_lincs = "https://ru.bidspirit.com" + item.find("a", class_="orange common-button ru").get("ng-href")
    print(lot_namber, " ", lot_name, " ", lot_sold, " ",lot_cost, " ", lot_lincs)

