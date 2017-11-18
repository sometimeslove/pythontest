# -*- coding:utf-8 -*-
#自己的解法
class Solution:
    def __init__(self):
        self._stack1 = []
        self._stack2 = []
    def push(self, node):
        if self._stack1 is None:
            return
        self._stack1.append(node)
    def pop(self):
        if len(self._stack1)==0:
            return None
        for i in range(len(self._stack1)-1):
            self._stack2.append(self._stack1.pop())
        s=self._stack1[0]
        self._stack1=[]
        for i in range(len(self._stack2)):
            self._stack1.append(self._stack2.pop())
        return s
#网上的解法
class Solution1:
    def __init__(self):
        self._stack1=[]
        self._stack2=[]
    def push(self,node):
        self._stack1.append(node)
    def pop(self):
        if self._stack2==[]:
            while self._stack1:
                self._stack2.append(self._stack1.pop())
        return self._stack2.pop()