# -*- coding:utf-8 -*-
import copy

# P5.1 把m的所有位merge到n中，位置由i，j给定 i=2 j=6
def BitsMerge(m,n,i,j):
    # 在python中，负数和0xffffffff按位与之后变成一个无符号数，二进制表示为编码形式
    # 这个非常重要，避免因为负数的负号导致错误
    allones = ~0b0 & 0xff
    left = allones << (j + 1)
    right = allones >> (8 - i)
    mask = left | right

    n &= mask
    m = m << i
    result = n | m
    print bin(result)

# P5.3 给定一个数，找出比它大一点和小一点的数，且这两个数的二进制表示中1的个数和原数相同
# 三步走
# （1）若想某个0翻转成1，必须将某个1翻转成0
# （2）如果0 - 1位于1 - 0的左边，数字就会变大
# （3）如果想让数字变大，又不至于太大，必须翻转最右边的0，且0右边还有1

def getNext(n):
    bn = n & 0xffffff
    str_bn = bin(bn)
    str_bn = str_bn[2:]
    #print bn
    length = len(str_bn)
    i = length - 1
    n_ones = 0
    n_zeros = 0
    p = 0
    while i >= 0:
        if str_bn[i] == "1":
            n_ones += 1
            if i-1 >= 0 and str_bn[i-1] == "0":
                p = i-1
                break
        else:
            n_zeros +=1
        i -= 1

    p = length - p - 1
    bn |= ( 1 << p)
    bn &= ~((1 << p)-1)
    bn |= (1 << (n_ones-1)) - 1

    return bn,bin(bn)



def getPrev(n):
    pass

# P5.5 编写函数，确定需要改变几个位，才能将整数A变成整数B
# 异或！！两个位异或结果为1，则说明不同；为0，说明相同
def checkDiffBits(A,B):
    count = 0
    c = A ^ B
    while c != 0:
        if c & 1 != 0:
            count += 1
        c = c >> 1

    return count
# P5.6 交换某整数的奇数位和偶数位
def swapNeiborBits(m):
    mask_even = 0b01010101
    mask_odd =  0b10101010
    m1 = (m & mask_even) << 1
    m2 = (m & mask_odd) >> 1
    return m1 | m2

# P5.7 找到0~N中缺少的数，采用位查看的方式
# ls列表是0~N所有的数字
def checkMissing(ls):
    INTEGER_SIZE = 8
    result = 0
    new_ls = copy.copy(ls)
    for col in range(INTEGER_SIZE):
        zeros = []
        ones = []
        for num in new_ls:
            if fetch(num,col) == 0:
                zeros.append(num)
            else:
                ones.append(num)
        if len(zeros) <= len(ones):
            new_ls = copy.copy(zeros)
            result = result | (0 << col)

        else:
            new_ls = copy.copy(ones)
            result = result | (1 << col)
    return bin(result),result

def fetch(bitInteger,col):
    if bitInteger & (1 << col) != 0:
        return 1
    else:
        return 0

# P5.8
def drawHorizonLine(screen,width,x1,x2,y):
    start_offset = x1 % 8
    fullByte_start = x1 / 8
    if start_offset != 0:
        fullByte_start += 1
    end_offset = x2 % 8
    fullByte_end = x2 / 8
    if end_offset != 7:
        fullByte_end -= 1
    for index in range(fullByte_start,fullByte_end+1):
        screen[(width/8)*y+index] = 0xff

    start_mask = 0xff >> start_offset
    end_mask = ~(0xff >> (end_offset+1))

    if x1 / 8 == x2 / 8:
        mask = start_mask & end_mask
        screen[(width/8)*y + x1 / 8] |= mask
    else:
        if start_offset != 0:
            screen[(width/8)*y+fullByte_start-1] |= start_mask
        elif end_offset != 7:
            screen[(width/8)*y+fullByte_end+1] |= end_mask




    pass
if __name__ == "__main__":


    #N = 0b10000000000
    #M = 0b10011
    #BitsMerge(M,N,2,6)

    #print getNext(13948)
    #print bin(13948)

    #A = 0b010010101
    #B = 0b100010011
    #m = 0b01011110
    #print bin(swapNeiborBits(m))
    #print fetch(0b001001,3)
    ls = [0b00000000,0b00000001,0b00000010,0b00000011,0b00000100,0b00000101,0b00000111]
    print checkMissing(ls)


