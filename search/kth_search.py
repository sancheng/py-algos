import random
import heapq

def kth_samllset_element(list, cmpFunc,k):
    if k<=0 or k >len(list):
        return None

    #random partition
    idx = random.randint(0, len(list) - 1)
    p = list[idx]
    list[idx],list[-1] = list[-1],list[idx]
    i = -1
    for j in range(0,len(list)-1):
        if cmpFunc(list[j],p) <=0:
            i+=1
            list[i],list[j] = list[j],list[i]
    list[i+1],list[-1] = list[-1],list[i+1]
    #check half of the list

    if i+2 == k:
        #print 'bingo'
        return list[i+1]

    elif i+2 < k:
        return kth_samllset_element(list[i+2:],cmpFunc,k-i-2)
    else:
        return kth_samllset_element(list[:i+1],cmpFunc,k)

'''
return result is not necessarily ordered
'''
def first_k_smallest_elements(list,k):
    if len(list) <= k:
        return list + []
    h = []

    for e in list:
        if len(h) < k:
            heapq.heappush(h,-1*e)
        else:
            if -1*e < h[0]:
                continue
            else:
                heapq.heappushpop(h,-1*e)

    return [-1*x for x in h]

#
print first_k_smallest_elements([32,13,11,4,22,12,6,12,7,34,267],3)
