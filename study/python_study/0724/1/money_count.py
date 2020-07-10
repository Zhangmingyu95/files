__author__ = 'mingyu.zhang'
def cal(x,y,z):
    money=int(x)
    for i in range(int(y)):
        money=money*(1+float(z)/365)
    return money
x=input('请输入本金：')
y=input('请输入天数：')
z=input('请输入利率：')
print(cal(x,y,z))
