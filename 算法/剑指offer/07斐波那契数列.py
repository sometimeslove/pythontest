# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        if n==1:
            return 1
        if n==2:
            return 1
        return self.Fibonacci(n)+self.Fibonacci(n-1)