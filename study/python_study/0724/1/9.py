__author__ = 'mingyu.zhang'
import time,_functools
def metric(fn):
    def wrapper(*args,**kw):
        start=time.time()
        z=fn(*args,**kw)
        end=time.time()
        print('%s executed in %.2f ms' % (fn.__name__, (end-start)*1000))
        return z
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
print(f)
s = slow(11, 22, 33)
print(s)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


