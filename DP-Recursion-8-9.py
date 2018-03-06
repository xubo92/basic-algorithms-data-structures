# -*- coding:utf-8 -*-

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

if __name__ == "__main__":
    #print GoUpStairs(6)
    print RobotMove(3,3)