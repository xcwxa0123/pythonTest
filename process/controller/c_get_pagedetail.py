from service import s_get_pagedetail
class getPageDetailController:
    def getPageDetail(self, page_href):
        resData = {}
        if not page_href:
            return { 'data': {}, 'code': 500, 'msg': '主键id有误' }
        try:
            resData = s_get_pagedetail.GetPageDetailService.get_page_detail(page_href)
        except Exception as e:
            return { 'data': {}, 'code': 500, 'msg': e }
        else:
            return { 'data': resData, 'code': 200, 'msg': 'success' }