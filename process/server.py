import flask, json, requests
from flask import request
from bs4 import BeautifulSoup

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
    res = requests.get("https://kakuyomu.jp/tags/%E7%99%BE%E5%90%88")
    con = res.content.decode('utf-8')
    soup = BeautifulSoup(con, 'html.parser')
    title_list = soup.find_all('div', class_='widget-work float-parent')
    print('soup====>', title_list)
    return json.dumps({ 'res': soup }, ensure_ascii=False)

if __name__ ==  '__main__':
    server.run(debug=True, port=8888, host='0.0.0.0')
    