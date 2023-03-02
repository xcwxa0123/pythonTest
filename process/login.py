import requests
from bs4 import BeautifulSoup
res = requests.get("https://kakuyomu.jp/tags/%E7%99%BE%E5%90%88")
con = res.content.decode('utf-8')
soup = BeautifulSoup(con, 'html.parser')
# name = soup.find('div', class_='widget-workCard-data')
print(soup)