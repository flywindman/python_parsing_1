import json         #импортируем модуль
import requests
from pprint import pprint #подключили Pprint для красоты выдачи текста
from openpyxl import Workbook
import re

url = "https://ru.bidspirit.com/services/catalogs/searchItemsWithSearchServer/?contentType=ART&futureAuctionsOnly=false&house=all&lang=ru&limit=10000&region=RU&skip=0&tag=books&templateCode=by_relevance&time=PAST"
src = requests.get(url).text

data = json.loads(src)

def cleaner (message):
        message = re.sub(r'\<[^>]*\>', '', message)
        message = re.sub(r'[\n\r]', '', message)
        message = re.sub(r'&nbsp;', ' ', message)
        message = re.sub(r'&raquo;', '"', message)
        message = re.sub(r'&laquo;', '"', message)
        message = re.sub(r'&times;', 'х', message)
        message = re.sub(r'&quot;', '"', message)
        message = re.sub(r'&amp;', '&', message)
        return message



#создание эксель файла
excel_file = Workbook()
excel_sheet = excel_file.create_sheet(title='bidspirit', index=0)

# создадим заголовки столбцов
excel_sheet['A1'] = 'Название'
excel_sheet['B1'] = 'Стартовая цена'
excel_sheet['C1'] = 'Цена продажи'
excel_sheet['D1'] = 'Описание'


for lot in range(9999):
    catalogKey = data['lotsData']['items'][lot]['ownerKey']
    cdnCacheVersion = data['lotsData']['auctions'][str(catalogKey)]['catalogCacheVersion']
    idInApp = data['lotsData']['items'][lot]['idInApp']
    
    payload = {'catalogKey': catalogKey, 'cdnCacheVersion': cdnCacheVersion, 'idInApp': idInApp, 'lang': 'ru',}
    thebook = requests.get('https://dnruccqi30a49.cloudfront.net/services/catalogs/getLotItemInfo', params=payload).text
    links = requests.get('https://dnruccqi30a49.cloudfront.net/services/catalogs/getLotItemInfo', params=payload)
        
    thebookjson = json.loads(thebook)
        
    try:
        description = thebookjson['description']        #описание
    except Exception: description = "нет описания"
    try:
        bookname = thebookjson['name']                      #название
    except Exception:
        try:
            bookname = re.match(r'(?:<[^>]*>)*([^<]*)', str(description)).group(1)
        except Exception: bookname = 'без имени'
    try:
        startPrice = thebookjson['startPrice']          #стартовая цена
    except Exception: startPrice = "нет стартовой цены"
    try:
        directSalePrice = thebookjson['directSalePrice']    #за сколько продан
    except Exception: directSalePrice = "не продался"

    bookname = cleaner(bookname)
    description = cleaner(description)
    
    book_rows = (bookname, startPrice, directSalePrice, description,)
    excel_sheet.append(book_rows)
    excel_file.save('bidspirits_baza_10000.xlsx')
    print(str(lot) + '...done...\n')
    