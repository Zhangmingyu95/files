__author__ = 'mingyu.zhang'
'''L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
L2 = sorted(L, key=by_name)
print(L2)'''

'''def createCounter():
    global i
    i=0
    def counter():
        global i
        i=i+1
        return i


    return counter



counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

print(counterA(),counterA())
print(counterB())
print(counterB())
print(counterB())
print(counterA())
counterC = createCounter()
print(counterC())
'''



L = list(filter(lambda n: n%2==1, range(1, 20)))
print(L)
