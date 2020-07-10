__author__ = 'mingyu.zhang'
# -*- coding: utf-8 -*-
'''from io import StringIO
'f=open('C:\\Users\\mingyu.zhang\\Desktop\\222.txt','r')
f=open('C:\\Users\\mingyu.zhang\\Desktop\\222.txt','r')
print(F)
d=open('C:\\Users\\mingyu.zhang\\Desktop\\222.txt','w')
D=d.write('hello world')
f=open('C:\\Users\\mingyu.zhang\\Desktop\\222.txt','r')

print(d.read())
f=StringIO()
f.write('Hello')
print(f.read())
'''

'''from io import StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
     s = f.readline()
     if s == '':
        break
     print(s.strip())'''

'''from io import BytesIO
f=BytesIO()
f.write('中文'.encode('utf-8'))
f.seek(0)
print(f.read())'''

'''import os

#os.mkdir(os.path.join(os.path.abspath('.'),'3'))
os.rmdir(os.path.join(os.path.abspath('..'),'3'))'''
'''import os
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])'''

'''import pickle
d='str'
print(pickle.dumps(d))
import pickle
import os
import json
obj = dict(name='小明', age=20)
s = json.dumps(obj,ensure_ascii=False)
print(s)

qwe='qwe'
print(qwe)
s=json.dumps(qwe)
print(s)
d=json.loads(s)
print(d)'''

import pickle
import json

class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age

def Stu2dict(std):
    return {'name':std.name,'age':std.age}
s=Student('kevin',24)
print(json.dumps(s,default=Stu2dict))
