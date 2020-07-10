
__author__ = 'mingyu.zhang'
def log(text):
    def decorator(func):
        def ww(*args,**kw):
            print('%s %s():' %(text,func.__name__))
            return func(*args,**kw)
        return ww
    return decorator

@log('execue')
def now():
    print('2019')
now()
now()

print("dont\'t be so hesitate")