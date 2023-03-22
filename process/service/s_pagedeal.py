import requests
from bs4 import BeautifulSoup
from service.s_base_service import BaseService
class PageDealService(BaseService):
    @classmethod
    def get_book_msg(cls, page_index):
        soup = cls().get_soup("https://kakuyomu.jp/tags/%E7%99%BE%E5%90%88?page={}".format(page_index))
        # 大模块
        moudle_list = soup.find_all('div', class_='widget-work float-parent')
        book_list = []
        for moudle in moudle_list:
            book_title = ''
            boot_auther = ''
            book_desc = ''
            book_href = ''
            # left_moudle = len(moudle.select('.float-left')) ? moudle.select('.float-left')[0] : None
            left_moudle = None if not len(moudle.select('.float-left')) else moudle.select('.float-left')[0]
            # print(left_moudle)
            if left_moudle:
                book_title = left_moudle.find('a', class_='widget-workCard-titleLabel bookWalker-work-title').text
                boot_auther = left_moudle.find('a', class_='widget-workCard-authorLabel').text
                book_desc = left_moudle.select('.widget-workCard-introduction a')[0].text
                book_href = left_moudle.find('a', class_='widget-workCard-titleLabel bookWalker-work-title')['href']
                boot_dist = {
                    'book_title': book_title,
                    'boot_auther': boot_auther,
                    'book_desc': book_desc,
                    'book_href': book_href 
                }
                book_list.append(boot_dist)
        print('book_list', book_list)
        return book_list