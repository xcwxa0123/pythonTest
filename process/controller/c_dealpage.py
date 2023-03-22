from service import s_pagedeal
class PageDealController:
    def pageDeal(self, page_index):
        book_msg_list = None
        msg = ''
        code = 0
        data = None
        if not page_index:
            page_index = 0
        try:
            book_msg_list = s_pagedeal.PageDealService.get_book_msg(page_index)
        except Exception as e:
            print(e)
            code = 500
            msg = e
            data = None
        else:
            code = 200
            msg = 'success'
            data = book_msg_list
        res = {
            'code': code,
            'msg': msg,
            'data': data
        }
        return res