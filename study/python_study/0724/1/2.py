__author__ = 'mingyu.zhang'
def findMinAndMax(L):
    Min=None
    Max=None
    if len(L) == 0:
        return (Min,Max)
    else:
        Min = L[0]
        Max = L[0]
        for l in L:
            if l < Min:
                Min = l
            if l > Max:
                Max = l
    return  (Min,Max)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')