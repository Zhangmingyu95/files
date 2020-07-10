__author__ = 'mingyu.zhang'
'''class Fib(object):
    def __init__(self):
        self.a,self.b=0,1

    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b = self.b,self.a + self.b
        if self.a > 10000:
            raise  StopIteration()
        return self.a

f=Fib()
for i in f:
    print(i)'''

'''class Get(object):
    def __getitem__(self, item):
        a,b = 1,1
        for i in range(item):
            a,b = b,a+b
        return a

get=Get()
print(get[10])'''

class fn(object):
    def __init__(self,name):
        self._name=name
    def __getattr__(self, item):
        if item == 'score':
            return 99
    def __call__(self, *args, **kwargs):
        return 11

f=fn('a')
print(f.score)
print(f())