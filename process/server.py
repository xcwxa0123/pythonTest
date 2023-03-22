import flask, json, requests
from flask import request
from controller import c_dealpage, c_get_pagedetail

server = flask.Flask(__name__)

@server.route('/login', methods=['GET', 'POST'])
def login():
    username = request.values.get('name')
    pwd = request.values.get('pwd')
    if username and pwd:
        res = { 'code': 200, 'msg': 'success'}
        return json.dumps(res, ensure_ascii=False)
    else:
        res = { 'code': -1, 'msg': 'error' }
        return json.dumps(res, ensure_ascii=False)

@server.route('/pageRes', methods=['GET'])
def pageRes():
    page_index = request.values.get('pageIndex')
    res = c_dealpage.PageDealController().pageDeal(page_index)
    return json.dumps(res, ensure_ascii=False)

@server.route('/getPageDetail', methods=['GET'])
def getPageDetail():
    page_href = request.values.get('pageHref')
    res = c_get_pagedetail.getPageDetailController().getPageDetail(page_href)
    return json.dumps(res, ensure_ascii=False)

if __name__ ==  '__main__':
    server.run(debug=True, port=8888, host='0.0.0.0')
    