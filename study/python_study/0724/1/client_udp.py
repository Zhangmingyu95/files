__author__ = 'mingyu.zhang'
import threading,socket,time

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    data=input()
    print('recive from server: %s' % s.recv(1024).decode('utf-8'))
    if data:
        s.sendto(data.encode('utf-8'),('127.0.0.1',9999))
        time.sleep(1)
    elif not data or data == 'exit':
        break
s.close()