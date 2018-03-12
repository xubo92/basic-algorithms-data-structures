# -*- coding:utf-8 -*-


# P11.1
# 给定两个排序后的数组A和B，其中A的末端有足够的缓冲空间容纳B。编写一个方法，将B合并入A并排序。

# lastA 是A中最后一个元素的位置，但不是A的最后一个空间位置
def AB_merge(a,b,lastA,lastB):


    mergeLast = (lastA + lastB)


    while lastA >= 0 and lastB >= 0:
        if a[lastA] >= b[lastB]:
            a[mergeLast] = a[lastA]
            mergeLast -= 1
            lastA -= 1
        else:
            a[mergeLast] = b[lastB]
            mergeLast -= 1
            lastB -= 1
    while lastB >= 0:
        a[mergeLast] = b[lastB]
        lastB -= 1

    return a

# P11.2 把字符串数组中的变位词排到一起挨着
# 方法一：构造自己的__cmp__函数，采用传统排序方案

def __cmp__(x,y):

    return cmp(sorted(x),sorted(y))
# 方法二，采用散列表
def anagramSort(ls):
    dic = dict()
    result=[]
    for it in ls:
        key = ''.join(sorted(it))
        if not dic.has_key(key):
            dic[key] = []
            dic[key].append(it)
        else:
            dic[key].append(it)


    for key in dic.iterkeys():
        for item in dic[key]:

            result.append(item)

    return result

if __name__ == "__main__":

    #a = [1,7,23,56,109,208,306,0,0,0,0]
    #b = [15,65,222]
    #print AB_merge(a,b,6,2)

    list = ["acre","triangle","race","integral","care","mountain"]
    #list = [1,100,1,20,1,43]
    #print sorted(list,__cmp__)
    print anagramSort(list)