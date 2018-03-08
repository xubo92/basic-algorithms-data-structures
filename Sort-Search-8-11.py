# -*- coding:utf-8 -*-

class MergeSort(object):
    def __init__(self,a):
        self.a = a
    def mergesort(self,first,last,tmp):
        if first < last:
            mid = (first + last) /2
            self.mergesort(first,mid,tmp)
            self.mergesort(mid+1,last,tmp)
            self.mergeArray(first,mid,last,tmp)

    # 重点在如何归在一起 好好理解
    def mergeArray(self,first,mid,last,tmp):
        i = first
        j = mid + 1
        k = 0
        while i <= mid and j <= last:
            if self.a[i] < self.a[j]:
                tmp[k] = self.a[i]
                k += 1
                i += 1
            else:
                tmp[k] = self.a[j]
                k += 1
                j += 1
        while i <= mid:
            tmp[k] = self.a[i]
            k += 1
            i += 1
        while j <= last:
            tmp[k] = self.a[j]
            k += 1
            j += 1

        for n in range(0,k):
            self.a[first + n] = tmp[n]
class QuickSort(object):
    def __init__(self,a):
        self.a = a
    # 快速排序 从右边优先开始扫描
    # 先前后交换，最后把停止位置的和基准点交换
    def quicksort(self,left,right):
        index = self.partition(left,right)
        if left < index - 1:
            self.quicksort(left,index-1)
        if index < right:
            self.quicksort(index,right)

    def partition(self,left,right):
        pivot = self.a[(left+right)/2]

        while left <= right:
            # 从右边先开始扫描
            while self.a[right] > pivot:
                right -= 1

            while self.a[left] < pivot:
                left += 1


            if left <= right:
                tmp = self.a[left]
                self.a[left] = self.a[right]
                self.a[right] = tmp
                left += 1
                right -= 1

        return left

class RadixSort(object):
    def __init__(self,a):
        self.a = a
        self.radix = 10
    def radixsort(self):
        buckets = [[] for i in range(self.radix)]
        for j in range(len(self.a)):
            mod = self.a[j] % self.radix
            buckets[mod].append(self.a[j])

    def __getmax(self):
        return max(self.a)
    def __getdigit(self):
        max_item = self.__getmax()
        digit = 1
        tmp = max_item // self.radix
        while tmp != 0:
            digit += 1
            tmp = tmp // self.radix

        return digit


if __name__=="__main__":
    a = [1,4,2,5,7,3,8,1,0,43,25,78,2,0,0]
    #tmp = [0 for i in range(len(a))]
    s = QuickSort(a)
    #s.mergesort(0,len(a)-1,tmp)
    s.quicksort(0,len(a)-1)
    print s.a