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
        c_digit = 1
        digit = self.__getdigit()
        temp = 1
        while c_digit <= digit:
            # 每经过一位 在桶里重新分配一遍
            for j in range(len(self.a)):
                mod = (self.a[j] // temp) % self.radix
                buckets[mod].append(self.a[j])
            self.a = []
            # 每次分配完，还要按照桶里的顺序弄回原数组 准备下次分配
            for bucket in buckets:
                for k in range(len(bucket)):
                    self.a.append(bucket[k])
            buckets = [[] for i in range(self.radix)]
            c_digit += 1
            temp *= self.radix

        print self.a
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

class BinarySearch(object):
    def __init__(self):
        pass
    # 重要 二分查找高效的基础 是原数组有序！！
    def binarysearch(self,a,x,low,high):
        if low > high:
            return -1

        mid = (low + high) / 2

        if x < a[mid]:
            return self.binarysearch(a,x,low,mid-1)
        elif x > a[mid]:
            return self.binarysearch(a,x,mid+1,high)
        else:
            return mid

class HeapSort(object):
    def __init__(self,heap):
        self.heap = heap
        self.heapsize = len(self.heap)
    def AdjustHeap(self,root,size):
        left = 2 * root +1
        right = left + 1
        larger = root
        # 要注意，两个if并列检查，比较了三个数，即父节点和两个子节点的大小，最大的那个当 larger。注意下一句的self.heap[larger]
        # 有可能是larger = left之后的新larger
        if left < size and self.heap[root] < self.heap[left]:
            larger = left
        if right < size and self.heap[larger] < self.heap[right]:
            larger = right
        if larger != root:
            self.heap[root],self.heap[larger] = self.heap[larger],self.heap[root]
            self.AdjustHeap(larger,size)

    def BuildHeap(self):
        for i in xrange((self.heapsize - 2)//2 , -1,-1):
            self.AdjustHeap(i,self.heapsize)

    def heapsort(self):
        self.BuildHeap()
        for i in xrange(self.heapsize-1,-1,-1):
            self.heap[0],self.heap[i] = self.heap[i],self.heap[0]
            self.AdjustHeap(0,i)
        return self.heap

if __name__=="__main__":
    a = [1,4,2,5,7,3,8,1,0,43,25,78,2,0,0,17264,16390]
    #x = 43
    #tmp = [0 for i in range(len(a))]
    #s = QuickSort(a)
    #s.mergesort(0,len(a)-1,tmp)
    #s.quicksort(0,len(a)-1)
    #rs = RadixSort(a)
    #rs.radixsort()
    #qs = QuickSort(a)
    #qs.quicksort(0,len(a)-1)
    #bs = BinarySearch()
    #print qs.a
    #print bs.binarysearch(qs.a,x,0,len(a)-1)
    hs = HeapSort(a)
    print hs.heapsort()