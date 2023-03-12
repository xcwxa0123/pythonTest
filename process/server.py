import flask, json, requests
from flask import request
from controller import c_dealpage

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
    print('pageIndex==========>', page_index)
    res = c_dealpage.PageDealController().pageDeal(page_index)
    return json.dumps(res, ensure_ascii=False)

if __name__ ==  '__main__':
    server.run(debug=True, port=8888, host='0.0.0.0')
    