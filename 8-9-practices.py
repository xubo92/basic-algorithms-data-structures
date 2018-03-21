# -*- coding:utf-8 -*-
import copy
import numpy as np

# P9.1 上楼梯问题
def GoUpStairs(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n >= 3:
        return GoUpStairs(n-1) + GoUpStairs(n-2) + GoUpStairs(n-3) + n


# P9.2 机器人在网格中的移动规划
def RobotMove(x,y):
    if x == 0 and y == 0:
        return 0
    elif x == 0 or y == 0:
        return 1
    else:
        return RobotMove(x-1,y) + RobotMove(x,y-1)

# x,y 从终点递到起点，最后还会归回来。这点尤其要注意。递归函数中的参数，都会归回开始的样子
# allpath是所有可能的路径
def RobotMotionPlanning(x,y,cpath,allpath,obstacles):
    p = (x,y)

    cpath.append(p)
    if x == 0 and y == 0:
        tmp = copy.copy(cpath)
        allpath.append(tmp)
        cpath[:] = []
        return True
    isValid = False
    if x > 0 and (x-1,y) not in obstacles:
        isValid = RobotMotionPlanning(x-1,y,cpath,allpath,obstacles)

    # 如果下面这句改成这样，就只返回一条路径 区别在于if语句对递归过程的限制条件
    '''
    if not isValid and (x,y-1) not in obstacles:
        isValid = RobotMotionPlanning(x, y - 1, cpath, allpath, obstacles)
    '''
    if y > 0 and (x,y-1) not in obstacles:
        isValid = RobotMotionPlanning(x,y-1,cpath,allpath,obstacles)
    if not isValid:
        cpath.remove(p)
    return isValid

# P9.3 魔术索引问题
# 简单版本：元素有序 且 都不重复
def FindMagicIndex(ls,first,last):

    mid = (first + last)/2
    if first > last:
        return -1
    if ls[mid] == mid:
        return mid
    elif ls[mid] > mid:
        return FindMagicIndex(ls,first,mid-1)
    else:
        return FindMagicIndex(ls,mid+1,last)
# P9.3 魔术索引问题
# 复杂版本：元素有序 且 存在重复

def FindMagicIndex_2(ls,first,last,allvalid):
    mid = (first+last)/2
    if first > last:
        return -1
    if ls[mid] == mid:
        allvalid.append(mid)
    else:
        FindMagicIndex_2(ls,first,min(ls[mid],mid),allvalid)

        FindMagicIndex_2(ls,max(ls[mid],mid),last,allvalid)

# P9.4 求解某集合的所有子集
def FindAllSubsets(ls,n):

    if n == 0:
        return [[]]

    else:
        result = FindAllSubsets(ls, n-1)
        new_result = copy.copy(result)
        for i in range(len(result)):
            temp = copy.copy(result[i])
            temp.append(ls[n - 1])
            new_result.append(temp)
        return new_result

# P9.5 求解某字符串的所有排列组合
def FindAllCombination(str,n):
    if n == 1:
        return [str[0]]
    else:
        result = FindAllCombination(str,n-1)
        new_result = []
        for i in range(len(result)):
            tmp = copy.copy(result[i])
            pos_num = len(tmp) + 1
            for j in range(pos_num):
                new_result.append(InsertIntoStr(str[n-1],tmp,j))
        return new_result
def InsertIntoStr(c,str,i):
    pos_num = len(str) + 1

    start = str[0:i]
    end = str[i:]
    return start + c + end




# P9.6 打印所有括号组合

# 从这个例子好好再理解一下递归解决问题的特点
# 事实上，递归只要发生在函数未结束的时候，就早晚会归到那个位置，继续进行下面的步骤。
# 也就是说，递归可以解决 多种可能分支（或者说指数型可能分支） 这种特点的问题
# 只需要归回来，再递出去 就可以了
def AddBrackets(strlist,leftrem,rightrem,str,count):
    if (leftrem < 0) or rightrem < leftrem:
        return
    if (leftrem == 0 and rightrem == 0):
        tmp_str = copy.copy(str)
        strlist.append(tmp_str)
    else:
        if (leftrem > 0):
            str[count] = "("
            AddBrackets(strlist,leftrem-1,rightrem,str,count+1)
        if (rightrem > leftrem):
            str[count] = ")"
            AddBrackets(strlist, leftrem, rightrem-1, str, count + 1)

# P9.7 实现颜色填充功能 针对某个点，向周围填充新颜色
def PaintFill(img,oldcolor,newcolor,point):
    x = point[0]
    y = point[1]


    if x >= img.rows or x < 0 or y >= img.cols or y < 0:
        return False

    if img[x,y] == oldcolor:
        img[x,y] = newcolor
        PaintFill(img,oldcolor,newcolor,(x,y+1))
        PaintFill(img, oldcolor, newcolor, (x, y - 1))
        PaintFill(img, oldcolor, newcolor, (x+1, y))
        PaintFill(img, oldcolor, newcolor, (x-1, y))

    return True

# P9.8
# P9.9 八皇后问题 要求各行、各列、各对角线都不能同时存在多于一个皇后
def EightQueens(posList,c_row,result):
    GRID_SIZE = 8
    if c_row == GRID_SIZE:
        result.append(copy.copy(posList))
    else:
        for col in range(GRID_SIZE):
            if Check_Valid(posList,c_row,col):
                posList[c_row] = col
                EightQueens(posList,c_row+1,result)

def Check_Valid(posList,c_row,col):
    for id in range(c_row+1):
        if posList[id] == col or abs(posList[id]-col) == abs(id - c_row):
            return False

    return True
def Print(result):

    board = np.zeros((8,8))
    for i in range(8):
        board[i][result[0][i]] = 1
    print board

# P9.10 搭出最高一堆箱子问题，其中箱子之间满足某些约束条件
# 实质上类似于最长递增子序列问题

def MakeBoxsMoreHigh(ls):
    ls.sort(key=lambda x:x[0])
    length = len(ls)
    # a 以ls中每个元素结尾的最长子序列长度
    a = [1 for i in range(length)]
    # b 前驱元素的位置数组
    b = [i for i in range(length)]
    max_num = 1
    max_index = 0

    for i in range(1, length):
        for j in range(0, i):
            if ls[i][1] >= ls[j][1] and ls[i][2] >= ls[j][2] and a[j] + 1 >= a[i]:
                a[i] = a[j] + 1
                b[i] = j

            if a[i] > max_num:
                max_num = a[i]
                max_index = i

    result = [() for i in range(max_num)]
    k = max_num - 1
    result[k] = ls[max_index]
    k = k - 1
    while b[max_index] != max_index:
        result[k] = ls[b[max_index]]
        max_index = b[max_index]
        k = k - 1

    return result, max_num

# P9.11 布尔表达式的组合表示问题



if __name__ == "__main__":
    '''
    ls = [-10,-5,2,2,2,3,4,7,9,12,13]
    allvalid = []
    FindMagicIndex_2(ls,0,len(ls)-1,allvalid)
    print allvalid
    '''

    #ls = [1,2,3]
    #print FindAllSubsets(ls,3)
    #s = "lily"
    #print s[5:]
    #print FindAllCombination(s,len(s))
    #posList = [-1 for i in range(8)]
    #result = []

    #EightQueens(posList,0,result)
    #Print(result)

    ls = [(10,5,4),(6,2,3),(13,4,1),(8,5,2),(11,6,5),(1,1,1)]
    print MakeBoxsMoreHigh(ls)