import requests
from bs4 import BeautifulSoup
import io


url = "https://ru.bidspirit.com/ui/catalog/auction/litfund/19913/1?lang=ru"
src = requests.get(url).text
soup = BeautifulSoup(src, "lxml")
print(soup)
with io.open("381.html", encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
print(soup)
