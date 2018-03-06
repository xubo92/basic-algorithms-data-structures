# -*- coding:utf-8 -*-


print bin((1 << 5)-1)


class BitOperation(object):
    def __init__(self,num):
        self.num = num
    # 获取第i位的值（二进制）
    def getAt(self,i):
        return ((1 << i) & self.num != 0)
    # 置位 （默认置1）
    def setAt(self,i):
        return (1 << i) | self.num
    def clearAt(self,i):
        return (~(1 << i)) & self.num
    # 更新 先清零再置位
    def updateAt(self,i):
        mask = (~(1 << i))
        return (mask & self.num) | (1 << i)

