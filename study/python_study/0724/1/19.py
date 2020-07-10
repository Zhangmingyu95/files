from multiprocessing import Pool,Process,Queue
import time,os,threading


'''def action(a,b):

    for i in range(b):
        print("%s第%d次输出%s" % (a,i,time.clock()))


if __name__=='__main__':
    pools=Pool(4)
    print(os.getpid())
    pools.apply_async(action,args=("进程一",50))
    pools.apply_async(action,args=("进程二",50))
    pools.apply_async(action,args=("进程三",50))
    pools.close()
    pools.join()
    print("done")'''

'''def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))

    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop)
t2=threading.Thread(target=loop)
t.start()

t2.start()
t.join()
t2.join()

print('thread %s ended.' % threading.current_thread().name)'''

'''def p1(q,i,t1):
    print("start to run takes")
    t1.start()
    t1.join()

def p2(q,i,t2):
    print("Stop running")
    t2.start()
    t2.terminate()

def t1(q):
    while 1:
        v=q.get()
    print("get %s" % v)

def g1(q,I):
    for i in range(I):
        v=q.put(i)
    print("put %s" % v)

if "__name__"== "__main__":
    q=Queue()
    p=Pool(2)
    th=threading.Thread(target=g1,args=(q,))
    th2=threading.Thread(target=t1,args=(q,50))
    p.apply_async(target=p1,args=(q,50,th))
    p.apply_async(target=p2,args=(q,50,th2))
    p.close()
    p.join()
    print("done")'''

import multiprocessing
from multiprocessing import Pool, Process
import threading

def loop(i):
    x = 0
    print('Thread - ',i)
    while True:
        x = x ^ 1

def proc(i, cpu_cout):
    print('Process: ',i)
    for i in range(cpu_cout*2):
        t = threading.Thread(target=loop, args=(i,))
        t.start()

if __name__ == '__main__':
    cpu_cout = multiprocessing.cpu_count()
    p = Pool(cpu_cout)
    for i in range(cpu_cout):
        p.apply_async(proc,args=(i, cpu_cout))
    p.close()
    p.join()


