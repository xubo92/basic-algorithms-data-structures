# -*- coding:utf-8 -*-
import Queue

class BinaryNode(object):
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

# 内容同8-1的HashtableBST
class BST(object):
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


def isBalance(bst):
    return


# 图的构建过程，不能用链表所用的简单node结构，因为图中节点之间的连接关系更为多样
# 图的构建采用邻接列表形式
class Graph(object):
    def __init__(self,NodeList,AdjacentList):
        # Nodelist: [a,b,c,d,e,f,g] = range(7)
        # adjacent list:[{c,d,e},{f,g},...]
        # 为了后续计算方便，nodelist中元素均从0按照升序排列，和下标一致
        self.nodelist = NodeList
        self.adjacentlist = AdjacentList
        self.visited = [False]* len(self.nodelist)

    def prints(self):
        return
    # 选择哪个顶点为下一个访问顶点依赖于邻居的存储顺序
    # 递归容易实现
    def DFS(self,root):
        if root not in self.nodelist:
            raise ValueError, "the start node is invalid"
        self.visit(root)
        self.visited[root] = True
        for n in self.adjacentlist[root]:
            if self.visited[n] == False:
                self.DFS(n)
        return
    def visit(self,node):
        print node

    # 非递归好实现
    def BFS(self,root):
        if root not in self.nodelist:
            raise ValueError, "the start node is invalid"
        q = Queue.Queue(maxsize=8)
        q.put(root)
        self.visited[root] = True
        while not q.empty():
            tmp = q.get()
            for i in self.adjacentlist[tmp]:
                if self.visited[i] == False:
                    self.visited[i] = True
                    q.put(i)
            self.visit(tmp)


if __name__ == "__main__":
    a,b,c,d,e,f,g,h = range(8)
    al = [{b, d, f},{c, d, e},{f},{e},{f},{h},{f},{g}]
    nl = [a,b,c,d,e,f,g,h]
    graph = Graph(nl,al)
    #graph.DFS(a)
    graph.BFS(a)
