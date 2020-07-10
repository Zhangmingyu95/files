__author__ = 'mingyu.zhang'
from collections import namedtuple
import collections
import hashlib
import itertools
import time

'''Point=namedtuple('point',['x','y'])
p=Point(1,2)
print(p.x)

c=collections.Counter()
for a in "qqqqqwwwweeeerrrtttyy":
    c[a]=c[a]+1
print(c)

hib=hashlib.md5()
hib.update('how to do'.encode('utf-8'))
print(hib.hexdigest())

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
def login(user, password):
   md5=hashlib.md5()
   md5.update(password.encode('utf-8'))
   return md5.hexdigest() == db[user]

assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

it=itertools.repeat((1,2,3))
for i in it:
    print(i)
    time.sleep(1)'''

c='a'
c.upper()
print(c.upper())


