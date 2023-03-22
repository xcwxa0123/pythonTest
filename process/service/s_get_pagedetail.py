import requests
from bs4 import BeautifulSoup
from service.s_base_service import BaseService
class GetPageDetailService(BaseService):
    @classmethod
    def get_page_detail(cls, page_href):
        soup = cls().get_soup("https://kakuyomu.jp{}".format(page_href))
        # author name
        author_name = soup.select('#workAuthor-activityName a')[0]
        # state number
        [number_of_episode, publish_state] = soup.select('.widget-toc-workStatus span')
        # last refresh time
        last_time = soup.select('.widget-toc-date time span')[0]
        # episode data
        epi_data = soup.select('.widget-toc-items.test-toc-items li')
        epi_list = cls().get_epilist(epi_data)
        return {
            'author_name': author_name.text,
            'number_of_episode': number_of_episode.text,
            'publish_state': publish_state.text,
            'last_time': last_time.text,
            'episode_data': epi_list,
        }


    def get_epilist(self, lst):
        result = {}
        current_key = None
        for index, item in enumerate(lst):
            if 'widget-toc-chapter' in item.attrs['class']:
                current_key = index
                result[current_key] = {
                    'mian_title': item.find('span').text,
                    'episode_list': []
                }
            elif current_key is not None:
                result[current_key]['episode_list'].append({
                    'episode_title': item.find('span').text,
                    'refresh_time': item.find('time').text,
                    'href': item.find('a')['href']
                })
        return [value for _, value in result.items()]


# GetPageDetailService.get_page_detail('/works/1177354054894027232')