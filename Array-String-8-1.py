# -*- coding:utf-8 -*-
# 实现一个散列表，采用拉链法解决collision。包括 增删查改 四种操作
# 从低到上需要三层数据结构：节点 Node； 链表Linkedlist；散列表hashtable

import copy

class Node(object):
    def __init__(self, key, value, nexT=None):
        self.key = key  #节点的主要特征属性
        self.value = value
        self.nexT = nexT

class Linkedlist(object):

    def __init__(self):
        self.head = Node(None,None,None)  #链表的主要特征属性

    def isEmpty(self):
        return self.head.nexT == None

    def put(self,key,value):

        temp = Node(key,value,None)
        found = False
        if self.isEmpty():
            self.head.nexT = temp
        else:
            current = self.head
            while current.nexT != None:
                current = current.nexT
                if current.key == key:
                    current.value = value
                    found = True
                    break
            if not found:
                current.nexT = temp


    def get(self,key):
        if self.isEmpty():
            raise ValueError, "%s is not in the linkedlist" %key
        else:
            current = self.head
            while current.key != key and current.nexT != None:
                current = current.nexT
            if current.nexT == None:
                if current.key == key:
                    return current.value
                else:
                    raise ValueError, "can't find value of the key %s" %key
            else:
                return current.value

    def delete(self,key):
        deleted = False
        if self.isEmpty():
            raise ValueError, "%s is not in the linkedlist" %key
        else:
            current = self.head
            pre = self.head
            while current.nexT != None:
                if current.key != key:
                    pre = current
                    current = current.nexT
                else:
                    pre.nexT = current.nexT
                    current.nexT = None
                    deleted = True
            if not deleted:
                if current.key != key:
                    raise ValueError, "%s is not in the linkedlist" % key
                else:
                    pre.nexT = None

    def prints(self):
        if self.isEmpty():
            raise ValueError, "an empty linkedlist"

        else:
            current = self.head
            print "(start)"
            while current.nexT != None:

                current = current.nexT
                print "-> (" + str(current.key) + "," + str(current.value) + ")"
            print "->(end)"


class HashTable(object):
    def __init__(self,size):
        self.size = size
        #self.array = [Linkedlist()] * self.size #散列表的主要特征属性
        self.array = [Linkedlist() for i in xrange(self.size)]
    # a simple hash function, only for 'int' key
    def hashfunc(self,key):
        index = key % self.size
        return index

    def put(self,key,value):
        index = self.hashfunc(key)
        if index not in range(self.size):
            raise ValueError,"Can't insert key %s" %key
        self.array[index].put(key,value)

    def get(self,key):
        index = self.hashfunc(key)
        if index not in range(self.size):
            raise ValueError,"Can't find key %s" %key
        return self.array[index].get(key)


    def delete(self,key):

        index = self.hashfunc(key)
        if index not in range(self.size):
            raise ValueError,"Can't find key %s" %key

        self.array[index].delete(key)


    def prints(self):
        for i in range(self.size-1):
            if not self.array[i].isEmpty():
                self.array[i].prints()

class BinaryNode(object):
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

# 使用二叉搜索树形结构实现hashtable， 优点在于不必一开始分配大数组
class HashTableBST(object):
    def __init__(self):
        #self.root = BinaryNode(None,None)
        self.root = None
    def isEmpty(self):
        return self.root == None

    # 循环的写法之所以不好写，是因为二叉树属于多分支扩展性结构
    def put(self,key,value):
        self.root = self._put(key,value,self.root)

    def _put(self,key,value,x):
        if x == None:
            return BinaryNode(key,value)
        if key < x.key:
            x.left = self._put(key,value,x.left)
        elif key > x.key:
            x.right = self._put(key,value,x.right)
        else:
            x.value = value
        return x


    def get(self,key):

        return self._get(key,self.root)
    def _get(self,key,x):
        if x == None:
            raise ValueError, "can't find the value of key %s" %key

        if key < x.key:
            self._get(key,x.left)
        elif key > x.key:
            self._get(key,x.right)
        else:
            return x.value

    def delete(self,key):
        self.root = self._delete(key,self.root)
    def _delete(self,key,x):
        if x == None:
            return None
        if key < x.key:
            x.left = self._delete(key,x.left)
        elif key > x.key:
            x.right = self._delete(key,x.right)
        else:
            if x.right == None: return x.left
            if x.left == None: return x.right
            # 这一步最为重要  仔细琢磨
            t = x
            x = self._min(t.right)

            x.right = self._delMin(t.right) # 和下一句的顺序不能颠倒,如果颠倒了，x的结构就变化了。画图就可看出原因
            x.left = t.left

        return x
    def min(self):
        return self._min(self.root).key
    def _min(self,x):
        if x.left == None:
            return x
        else:
            return self._min(x.left)

    def delMin(self):
        self.root = self._delMin(self.root)
    def _delMin(self,x):
        if x.left == None:
            return x.right

        x.left = self._delMin(x.left)
        return x

    def prints(self):
        self._prints(self.root)
    def _prints(self,x):
        if x == None:
            return
        if x.left != None:
            self._prints(x.left)
        print "key:",x.key
        print "value:",x.value
        if x.right != None:
            self._prints(x.right)


class DynamicArray(object):
    def __init__(self):
        self.size = 10
        self.array = self.size * [None]
        self.p = -1
    def isFull(self):
        return self.p == self.size - 1
    def extendStorage(self):
        self.size *= 2
        temp = self.size * [None]
        for i in range(len(self.array)):
            temp[i] = self.array[i]
        self.array = copy.copy(temp)

    def add(self,value):
        if self.isFull():
            self.extendStorage()

        self.p += 1
        self.array[self.p] = value

    def delete(self,index):
        if index not in range(self.size):
            raise ValueError,"index out of range"
        self.array[index] = None

    def set(self,index,value):
        if index not in range(self.size):
            raise ValueError,"index out of range"
        self.array[index] = value
    def get(self,index):
        if index not in range(self.size):
            raise ValueError,"index out of range"

        return self.array[index]
    def prints(self):
        for i in range(len(self.array)):
            print self.array[i]




    '''
    a = Linkedlist()
    a.put(2,5)
    a.put(3,7)
    a.put(10,20)

    a.prints()

    print a.get(2)
    print a.get(3)
    print a.get(10)

    a.delete(4)
    a.prints()
    
    
    b = HashTableBST()
    b.put(1,1)
    b.put(2,2)

    b.put(10,20)
    b.put(7,7)
    b.put(0,20)





    b.delete(1)
    b.delete(7)
    b.delete(2)

    b.get(10)
    b.get(5)
    b.prints()
    
    da = DynamicArray()
    da.add(1)
    da.add(2)
    for i in range(8):
        da.add(i)
    da.add(8)

    da.delete(4)

    da.set(4,10000)
    da.get(5)
    da.prints()
        '''
