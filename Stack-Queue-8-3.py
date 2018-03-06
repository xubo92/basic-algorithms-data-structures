# -*- coding:utf-8 -*-

class Node(object):
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Stack(object):
    def __init__(self):

        self.top = Node()

    def isEmpty(self):
        return self.top.next == None

    def pop(self):
        if self.isEmpty():
            raise ValueError, "No element in stack"
        data = self.top.data
        self.top = self.top.next
        return data

    def push(self,data):
        new = Node(data)
        new.next = self.top
        self.top = new


    def peek(self):

        if self.isEmpty():
            raise ValueError, "No element in stack"
        return self.top.data

    def prints(self):
        if self.isEmpty():
            return
        cur = self.top
        while cur.next != None:
            print cur.data
            cur = cur.next

class Queue(object):
    def __init__(self):
        self.first = None
        self.last = None
    def isEmpty(self):
        return self.first == None and self.last == None
    def Enqueue(self,data):
        new = Node(data)
        if self.isEmpty():
            self.first = new
            self.last = new
        else:
            self.last.next = new
            self.last = new

    def Dequeue(self):
        if self.isEmpty():
            raise ValueError, "No element in queue"
        data = self.first.data
        temp = self.first.next
        self.first = temp
        return data
    def prints(self):
        if self.isEmpty():
            return
        cur = self.first
        while cur != self.last:
            print cur.data
            cur = cur.next
        print cur.data

if __name__ == '__main__':
    s = Stack()
    q = Queue()
    '''
    s.push(1)
    s.push(2)
    s.push(3)

    s.pop()
    s.pop()
    s.prints()
    '''
    q.Enqueue(10)
    q.Enqueue(20)
    q.Enqueue(30)
    q.Dequeue()
    q.Dequeue()
    q.prints()
