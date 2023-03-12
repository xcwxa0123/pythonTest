import requests
from bs4 import BeautifulSoup
res = requests.get("https://kakuyomu.jp/tags/%E7%99%BE%E5%90%88")
con = res.content.decode('utf-8')
soup = BeautifulSoup(con, 'html.parser')
# 大模块
moudle_list = soup.find_all('div', class_='widget-work float-parent')
for moudle in moudle_list:
    book_title = ''
    boot_auther = ''
    book_desc = ''
    book_href = ''
    # left_moudle = len(moudle.select('.float-left')) ? moudle.select('.float-left')[0] : None
    left_moudle = None if not len(moudle.select('.float-left')) else moudle.select('.float-left')[0]
    # print(left_moudle)
    if left_moudle:
        book_title = left_moudle.find('a', class_='widget-workCard-titleLabel bookWalker-work-title').contents[0]
        boot_auther = left_moudle.find('a', class_='widget-workCard-authorLabel').contents[0]
        book_desc = left_moudle.find('p', class_='widget-workCard-introduction').contents[0].contents[0]
        book_href = left_moudle.find('a', class_='widget-workCard-titleLabel bookWalker-work-title')['href']
        boot_dist = {
            'book_title': book_title,
            'boot_auther': boot_auther,
            'book_desc':  book_desc,
            'book_href':book_href 
        }
        print(boot_dist)