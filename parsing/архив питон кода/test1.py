import requests
from bs4 import BeautifulSoup
def get_data(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0"
        }

    req = requests.get(url, headers)

    with open("projects.html", "w") as file:
        file.write(req.text)

get_data("https://ru.bidspirit.com/ui/catalog/auction/litfund/19913/1?lang=ru")
