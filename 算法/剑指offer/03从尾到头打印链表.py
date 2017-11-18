#!/usr/bin/env python3
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def printListFromTailToHead(self, listNode):
        str =[]
        head = listNode
        while head is not None:
            str.insert(0, head.val)
            head = listNode.next
        return str
if __name__=='__main__':
    try:
        S=Solution()
        array=input('请输入')
        print(S.printListFromTailToHead( array))
    except:
        pass