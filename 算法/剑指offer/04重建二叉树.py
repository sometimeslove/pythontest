#!/usr/bin/env python3
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def reConstructBinaryTree(self, pre, tin):
        node =TreeNode(pre[0])
        index = tin.index(pre[0])
        if len(pre)==0:
            return None
        if len(pre)==1:
            return pre[0]
        tinleft = tin[:index]
        tinright = tin[index+1:]
        preleft = pre[1:index+1]
        preright = pre[index+1:]
        node.left =self.reConstructBinaryTree(preleft,tinleft)
        node.right =self.reConstructBinaryTree(preright,tinright)
        return node
if __name__=='__main__':
    try:
        S=Solution()
        array1=input('请输入1')
        array2=input('请输入2')
        node = S.reConstructBinaryTree( array1,array2)
        print(node)
    except:
        pass