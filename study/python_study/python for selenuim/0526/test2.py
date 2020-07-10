__author__ = 'mingyu.zhang'

data=[2131,24,12,5,125,345,23523,63,216,431,342,2,424,62,3462,3462,34,6234,123,5234,63,64,3,63,4,6]

def lists(args:list):
    for i in range(len(args)):
        for j in range(len(args)-i-1):
            if args[j] > args[j+1]:
                args[j+1],args[j]=args[j],args[j+1]
    return args

def half(args:list,num):
    if len(args) == 0:
        print("列表为空")
    else:
        left = 0
        right = len(args) -1
        while(left<=right):
            mid = int((left+right)/2)
            if(args[mid] == num):
                return mid
if __name__ == "__main__":
    print(lists(data))