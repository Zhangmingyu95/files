__author__ = 'mingyu.zhang'


def method(lists):
    lengh = len(lists)
    for i in range(lengh):
        min_id=i
        for j in range(i+1,lengh):
            if lists[min_id] > lists[j]:
                min_id=j
        lists[i], lists[min_id] = lists[min_id],lists[i]
    return lists

if __name__ == '__main__':
   data=[23,123,52,5235,12,42,13,43]
   print(method(data))