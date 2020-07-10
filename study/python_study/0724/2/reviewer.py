__author__ = 'mingyu.zhang'
import pickle,datetime

from _functools import reduce
print("hello,%s" % "world")
print("{0} is s {1:.2f}".format("math",77.88))
def person(name,age,**kw):
    print("name:",name,"age:",age,'other:',kw)
person('kevin',22,sex='male')

def function1(add,age=1,*args,cuty,moce):
    print(str(age)+cuty)
    pass
function1("ni",2,cuty="fuck",moce="you")
world = "world"
print("hello "+world)
i=(x*2 for x in [1,2,3] if x > 0)
m=next(i)
m2=next(i)
print(m,m2)
def mapfuc(x,y):
    return x*y
#ma=map(mapfuc,(1,2,3,4,5))
#print(list(ma))
re=reduce(mapfuc,(1,2,3,4,5))
print(re)
l1=sorted(['1','2','3','4','5'])
print(l1)

class Person(object):
    def __init__(self,age,sexual):
        self.sexual=sexual
        self.age=age

    def Eat(self):
        self.food+=1

    def __str__(self):
        return 'fuck'

    def __iter__(self):
        return self

    def __next__(self):
        self.age+=1
        if self.age >100:
            raise StopIteration()
        return self.age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,value):
        try:
            if not isinstance(value,int):
                raise ValueError('enter the right value')
            if value < 0 or value > 100:
                raise ValueError('value error')
        finally:
            self._age=value


Sb=Person(1,'female')
Sb.food=1
while (True):
    Sb.Eat()
    if Sb.food >10:
        break
print(Sb.food)
Sb.age=2
print(Sb)
for i in Person(1,'male'):
    print(i)

class FoodError(ValueError):
    pass
def food():
    if 1==1:
        raise FoodError
food()

with open('.\签名.png','rb')as f:
    print(f.read())

with open('review.txt','wb') as d:
    pickle.dump(Sb,d)

