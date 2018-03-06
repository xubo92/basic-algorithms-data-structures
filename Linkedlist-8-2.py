# -*- coding:utf-8 -*-
class BiNode(object):
    def __init__(self,data=None):
        self.data = data
        self.front = None
        self.back = None
class BiLinkedlist(object):
    def __init__(self):
        self.head = BiNode()
        self.tail = BiNode()
        self.head.back = None
        self.tail.front = None
        self.head.front = self.tail
        self.tail.back = self.head
        self.size = 0
    def isEmpty(self):
        return self.head.front == self.tail
    # 尾部插入
    # 双向链表在尾部插入时比单向链表更快捷，因为可以直接找tail节点
    def insert(self,data):
        new = BiNode(data)
        prev_tail = self.tail.back
        self.tail.back = new
        new.front = self.tail
        prev_tail.front = new
        new.back = prev_tail
        self.size += 1

    # 单向链表删除节点需要时刻判断空指针，而双向链表因为有了tail节点，则可以避免这个
    def delete(self,pos):
        if pos not in range(self.size):
            raise ValueError, "index out of range"
        cur = self.head.front
        cur_pos = 0
        while cur_pos < pos and cur != self.tail:
            cur = cur.front
            cur_pos += 1
        prev = cur.back
        next = cur.front
        prev.front = next
        next.back = prev
        cur.back = None
        cur.front = None
        print "the data which was deleted is %d" %cur.data
        self.size -= 1
        return cur.data
    def get(self,pos):
        if pos not in range(self.size):
            raise ValueError, "index out of range"
        cur = self.head.front
        cur_pos = 0
        while cur_pos < pos and cur != self.tail:
            cur = cur.front
            cur_pos += 1
        return cur.data
    def set(self,pos,data):
        if pos not in range(self.size):
            raise ValueError, "index out of range"
        cur = self.head.front
        cur_pos = 0
        while cur_pos < pos and cur != self.tail:
            cur = cur.front
            cur_pos += 1
        cur.data = data
    def prints(self):
        cur = self.head.front
        cur_pos = 0
        while cur_pos <= self.size - 1:
            print cur.data
            cur = cur.front
            cur_pos += 1

if __name__ == '__main__':
    bl = BiLinkedlist()
    bl.insert(100)
    bl.insert(200)
    bl.insert(1)
    bl.insert(89)
    bl.delete(2)
    bl.delete(0)
    bl.prints()
    # print bl.size