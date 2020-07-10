__author__ = 'mingyu.zhang'


a=[23,55,1,43,64,12,34,54]

for i in range(a.__len__()):
    len=a.__len__()
    for k in range(len-i-1):
         if a[k] > a[k+1]:
              b = a[k]
              a[k] = a[k+1]
              a[k+1] = b
         else:
             continue
print(a)

def find_number(target_list,target_number):
    if(len(target_list)==0):
        print("为空")
    else:
        left=0
        right=len(target_list)-1
        while(left<=right):
            mid=int((left+right)/2)
            if(target_list[mid]==target_number):
                return mid
            elif(target_list[mid]<target_number):
                 left=mid+1
            else:
                 right=mid-1
        return -1
