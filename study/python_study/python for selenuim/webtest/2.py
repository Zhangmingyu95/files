__author__ = 'mingyu.zha'

import time
import threading

def sleeping():
    print('i am sleeping at'+time.ctime())
    time.sleep(2)

def playing():
    print('I am playing at'+ time.ctime())
    time.sleep(4)

if __name__ == '__main__':
    theads=[]
    t1=threading.Thread(target=sleeping(),args=())
    t2=threading.Thread(target=playing(),args=())
    theads.append(t1)
    theads.append(t2)
    for i in theads:
        i.start()
        i.join()

    sleeping()
    playing()
    print('end at'+time.ctime())