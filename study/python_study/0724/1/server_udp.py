__author__ = 'mingyu.zhang'
import socket,threading,time

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',9999))

def th(data,add,ti):
    while True:
        wd=input()
        if wd:
            s.sendto(('from server:%s' % wd).encode('utf-8'),add)
            print("send done")
        elif not wd or time.time()-ti > 10:
            s.sendto(('you have lost the connection from server'.encode('utf-8')),add)
            break

while True:
    data,add=s.recvfrom(1024)
    ti=time.time()
    if data:

        print("recive from client:%s" % data.decode('utf-8'))
        t=threading.Thread(target=th,args=(data,add,ti))
        t.start()
        t.join()


