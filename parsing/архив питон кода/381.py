import io
import requests
from bs4 import BeautifulSoup
# req = requests.get(url, headers)
 
#with open("381.html") as file:
#   src = file.read()
with io.open("381.html", encoding='utf-8') as file:
    src = file.read()
    

soup = BeautifulSoup(src, "lxml")

#title = soup.title.text
#print(title)

books = soup.find_all("div", class_="item ng-scope ng-isolate-scope pc-item")

for item in books:
    lot_name = item.find("span", class_="lot-name").text
    print(lot_name)
    lot_namber = item.find("span", class_="lot-number").text
    lot_sold = item.find("div", class_="text").text
    lot_cost = item.find("div", class_="lot-price-row ng-scope").text
    lot_lincs = "https://ru.bidspirit.com" + item.find("a", class_="orange common-button ru").get("ng-href")
    print(lot_namber, " ", lot_name, " ", lot_sold, " ",lot_cost, " ", lot_lincs)

