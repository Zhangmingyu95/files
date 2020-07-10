__author__ = 'mingyu.zhang'
from functools import reduce

'''DIGITS={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2num(s):
    def fn(x,y):
        return x*10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn,map(char2num,s))
    '''

'''def char2num(s):
    D={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return D[s]
print(list(map(char2num,'123')))
'''

'''
def normalize(name):
   return name.capitalize()
L1 = [input(), input(), input()]
L2 = list(map(normalize, L1))
print(L2)
'''

'''def cal(a,b):
    return  a*b
def prod(L):
    return reduce(cal,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
    '''

def str2float(s):
    D={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    S=s.split('.',1)

    def str2num(s):
        return D[s]
    def fn(x,y):
        return 10*x+y



    L1=map(str2num,S[0])
    L2=list(map(str2num,S[1]))
    return reduce(fn,L1)+reduce(fn,L2)/10**len(list(L2))
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
