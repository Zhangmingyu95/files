__author__ = 'mingyu.zhang'

import socket,threading,time


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
print(s.recv(1024).decode('utf-8'))
for i in ['1','2','3']:
    s.send(i.encode('utf-8'))
    #time.sleep(1)
    #print(s.recv(1024).decode('utf-8'))

s.send('exit'.encode('utf-8'))
s.close()
'''s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()'''
