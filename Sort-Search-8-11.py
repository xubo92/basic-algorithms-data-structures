# -*- coding:utf-8 -*-


def mergesort(a,first,last,tmp):
    if first < last:
        mid = (first + last) /2
        mergesort(a,first,mid,tmp)
        mergesort(a,mid+1,last,tmp)
        mergeArray(a,first,mid,last,tmp)
# 重点在如何归在一起 好好理解
def mergeArray(a,first,mid,last,tmp):
    i = first
    j = mid + 1
    k = 0
    while i <= mid and j <= last:
        if a[i] < a[j]:
            tmp[k] = a[i]
            k += 1
            i += 1
        else:
            tmp[k] = a[j]
            k += 1
            j += 1
    while i <= mid:
        tmp[k] = a[i]
        k += 1
        i += 1
    while j <= last:
        tmp[k] = a[j]
        k += 1
        j += 1

    for n in range(0,k):
        a[first + n] = tmp[n]



if __name__=="__main__":
    a = [1,4,2,5,7,3,8,1,0,2,9,4,68,3,52]
    tmp = [0 for i in range(len(a))]
    mergesort(a,0,len(a)-1,tmp)
    print a