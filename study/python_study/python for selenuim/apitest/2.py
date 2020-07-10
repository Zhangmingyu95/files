__author__ = 'mingyu.zhang'
import os

data=[1,1]
data=list(set(data))
print(data)

os.remove('re')
with open('log.txt','r') as f:
    data=f.readlines()
    data=data[1:]
print(data)
dic1={} #key为IP
dic2={} #key为URL

for i in data:
    a=i.split()
    b=a[0]
    c=a[1]
    dic1[b]=c
    dic2[c]=b
with open('re','a')as f:
    f.write('URL     IP\n')

for i in dic2:
    count=0
    for j in dic1:
            if dic1[j]== i:
                count=count+1
    with open('re','a')as f:
        f.write(i+'     '+str(count)+'\n')