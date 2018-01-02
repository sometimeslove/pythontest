# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def Merge(self, pHead1, pHead2):
        # write code here
        node = ListNode(90)
        while pHead1 and pHead2:
            if pHead1.val<pHead2.val:
                node.val = pHead1.val
                pHead1 = pHead1.next
            else:
                node.val = pHead2.val
                pHead2 = pHead2.next
            node = node.next
        node.next = pHead1 or pHead2
        return node