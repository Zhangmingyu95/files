__author__ = 'mingyu.zhang'
from contextlib import contextmanager
from urllib import request
import json
'''
class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

with create_query('Bob') as q:
    q.query()

with request.urlopen('http://10.3.2.102:6691/zh-CN/MainFrame/ShowImg?resCode=Diagnosis_Manager&treeCode=100002') as f:
    data = f.read()
    print('Status:', f.status)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))'''

def fetch_data(url):
    with request.urlopen(url) as f:
        data=f.read()
    return json.loads(data)

# 测试
URL = 'https://www.easy-mock.com/mock/5cbec5d8bfb3b05625e96633/dreamlf/urllibTest'
data = fetch_data(URL)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')

