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

# P 11.3 数组内容旋转后，找到某个值所在的位置
# 该题最大的特点，就是旋转后的数组，会有两段正常顺序部分（升序），长度不同。为了使用二分法查找，需要确定中间元素属于哪一段。
# 难点在于当中间元素和两头的元素都相同，无法判断中间元素属于哪一段的时候，就两边都搜素。
def SearchRotatedList(ls,left,right, item):

    mid = (left + right)/2

    if item == ls[mid]:
        return mid
    if right < left:
        return -1

    if ls[mid] > ls[left]:
        if item >= ls[left] and item <= ls[mid]:
            return SearchRotatedList(ls,left,mid-1,item)
        else:
            return SearchRotatedList(ls, mid+1, right, item)
    elif ls[mid] < ls[left]:
        if item >= ls[mid] and ls <= ls[right]:
            return SearchRotatedList(ls,mid+1,right,item)
        else:
            return SearchRotatedList(ls, left, mid-1, item)
    elif ls[mid] == ls[left]:
        result = SearchRotatedList(ls,left,mid-1,item)
        if result == -1:
            return SearchRotatedList(ls,mid+1,right,item)
        else:
            return result

    return -1

# P11.4 新概念 外部排序
# 即待排序内容过大，不能全部载入内存，需要分块处理
# http://blog.csdn.net/jeason29/article/details/50474772

# P11.5
def SearchwithBlanks(ls,left,right,item):

    if left > right:
        return -1
    mid = (left + right)/2

    if ls[mid] == " ":
        i = mid - 1
        j = mid + 1
        while (True):
            if i < left and j > right:
                return -1
            if i >= left and ls[i] != " ":
                mid = i
                break
            elif j <= right and ls[j] != " ":
                mid = j
                break
            else:
                i -= 1
                j += 1

    if ls[mid] == item:
        return mid
    elif cmp(ls[mid],item) > 0 :
        return SearchwithBlanks(ls,mid+1,right,item)
    elif cmp(ls[mid],item) < 0:
        return SearchwithBlanks(ls, left, mid-1, item)

    return -1

# P11.6 查找某升序M*N矩阵中的某一元素
# (0,0) -> (3,1)
def SearchMatrix(mat,origin,dest,item):
    row = dest[0] - origin[0]
    col = dest[1] - origin[1]
    if not (row >= 0 and col >= 0 and row < len(mat) and col < len(mat[0])):
        return -1

    if row == col:
        i = origin[0]
        j = origin[1]
        while mat[i][j] < item and i <= dest[0] and j <= dest[1]:
            i += 1
            j += 1
        if mat[i][j] == item:
            return (i,j)
        else:
            result = SearchMatrix(mat,(i,origin[0]),(dest[0],j-1),item)
            if result == -1:

                return SearchMatrix(mat,(origin[0],j),(i-1,dest[1]),item)
            else:
                return result

    elif row > col:
        Second_Mat_Origin = (min(row,col) + 1, 0)
        Second_Mat_Dest = (dest[0], dest[1])
        return SearchMatrix(mat, Second_Mat_Origin, Second_Mat_Dest, item)
    else:
        Second_Mat_Origin = (0,min(row,col)+1)
        Second_Mat_Dest = (dest[0], dest[1])
        return SearchMatrix(mat, Second_Mat_Origin, Second_Mat_Dest, item)

# P11.7 最长递增子序列问题
# 基本解法 复杂度 O(N^2)
def LongestIncresingSubSeq(ls):

    length = len(ls)
    # a 以ls中每个元素结尾的最长子序列长度
    a = [1 for i in range(length)]
    # b 前驱元素的位置数组
    b = [i for i in range(length)]
    max_num = 1
    max_index = 0

    for i in range(1,length):
        for j in range(0,i):
            if ls[i] >= ls[j] and a[j] + 1 >= a[i]:
                a[i] = a[j] + 1
                b[i] = j

            if a[i] > max_num:
                max_num = a[i]
                max_index = i

    result = [0 for i in range(max_num)]
    k = max_num-1
    result[k] = ls[max_index]
    k = k - 1
    while b[max_index] != max_index:
        result[k] = ls[b[max_index]]
        max_index = b[max_index]
        k = k - 1


    return result,max_num



if __name__ == "__main__":


    #a = [1,7,23,56,109,208,306,0,0,0,0]
    #b = [15,65,222]
    #print AB_merge(a,b,6,2)

    #list = ["acre","triangle","race","integral","care","mountain"]
    #list = [1,100,1,20,1,43]
    #print sorted(list,__cmp__)

    #ls = [10,15,20,0,5]
    #ls = [50,5,20,30,40]
    #ls = [2,2,2,3,4,2]

    #ls = ["amy ","stephen","lily","want"]

    #print SearchwithBlanks(ls,0,len(ls)-1,"gorgerous")

    #Mat = [[15,20,30,40],[20,35,36,41],[30,55,57,58],[40,80,91,92]]
    #print SearchMatrix(Mat,(0,0),(3,3),15)

    list = [35,36,39,3,15,6,42,41]
    print LongestIncresingSubSeq(list)