__author__ = 'mingyu.zhang'
import threading

'''# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()'''

import random, time, queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

def sendtask():
    return task_queue
def gettask():
    return result_queue
# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
def test():
        QueueManager.register('get_task_queue', callable=sendtask)
        QueueManager.register('get_result_queue', callable=gettask)
        # 绑定端口5000, 设置验证码'abc':
        manager = QueueManager(address=('', 5000), authkey=b'abc')
        # 启动Queue:
        manager.start()
        # 获得通过网络访问的Queue对象:
        task = manager.get_task_queue()
        result = manager.get_result_queue()
        # 放几个任务进去:
        for i in range(10):
            n = random.randint(0, 10000)
            print('Put task %d...' % n)
            task.put(n)
        # 从result队列读取结果:
        print('Try get results...')
        for i in range(10):
            r = result.get(timeout=10)
            print('Result: %s' % r)
        # 关闭:
        manager.shutdown()
        print('master exit.')

if "__name__"=="__main__":
    freeze_support()
    test()