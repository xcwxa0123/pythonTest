import requests

# 引入 requests，实现请求
URL = 'http://c.biancheng.net/uploads/course/python_spider/191009.html'
# 输入在浏览器的网址
res = requests.get(URL)
res.encoding = res.apparent_encoding
# 发送 GET 方式的请求，并把返回的结果(响应)存储在 res 变量里头
print(res.html)
