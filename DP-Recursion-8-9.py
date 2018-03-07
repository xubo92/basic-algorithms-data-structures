# -*- coding:utf-8 -*-
import copy
# 动态规划问题就是递归解法外加保存中间值

# 上楼梯问题
def GoUpStairs(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n >= 3:
        return GoUpStairs(n-1) + GoUpStairs(n-2) + GoUpStairs(n-3) + n

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

if __name__ == "__main__":
    #print GoUpStairs(6)
    #print RobotMove(3,3)
    '''
    string = ["" for i in range(2*2)]
    l = list()
    AddBrackets(l,2,2,string,0)
    print l
    '''
    path = list()
    allpath = list()
    obstacles = [(1,1)]
    RobotMotionPlanning(2,2,path,allpath,obstacles)
    print allpath
