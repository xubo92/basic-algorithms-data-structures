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

def __cmp__(x,y):

    if sorted(x)!= sorted(y):
        if x[0] < y[0]:
            return -1
        else:
            return 1
    else:
        return 0


if __name__ == "__main__":

    #a = [1,7,23,56,109,208,306,0,0,0,0]
    #b = [15,65,222]
    #print AB_merge(a,b,6,2)

    list = ["acre","triangle","race","integral","care","mountain"]

    print sorted(list,__cmp__)