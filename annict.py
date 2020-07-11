import requests
import json
from bs4 import BeautifulSoup
import sys

def scrape(r):
    soup = BeautifulSoup(r.text , "html.parser")
    titles = soup.find_all("a", {"class": "d-inline-block"})
    for atag in titles:
        with open('./result.txt', 'a') as f:
            print(atag.get_text(strip=True), file=f)
    return len(titles)

args = sys.argv

id_string = args[1]
print(id_string)
url = "https://annict.jp/@" + id_string + "/watched"
i = 0
while True:
    i += 1
    r = requests.get(url + "?page=" + str(i))
    length = scrape(r)
    if length < 2:
        break
