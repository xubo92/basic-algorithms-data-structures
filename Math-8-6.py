# -*- coding:utf-8 -*-

class PrimeCheck(object):
    def __init__(self,max):

        self.max = max
    # 实现埃拉托斯特尼筛法 有个技巧 就是 把max看成数组的最大index，数组的内容用布尔值表示，表明该index是否是素数
    def Eratosthenes(self):
        l = [True for i in range(self.max+1)]
        l[0] = l[1] = False
        prime = 2


        while prime <= self.max:
            if l[prime] == True:
                for j in range(prime * prime, self.max + 1, prime):
                    l[j] = False
                prime += 1
            else:
                prime += 1

        for i in range(self.max+1):
            if l[i] == True:
                print i


if __name__ == "__main__":
    pc = PrimeCheck(20)
    pc.Eratosthenes()