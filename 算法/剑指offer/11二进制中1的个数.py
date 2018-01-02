#!/usr/bin/env python3
# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        return sum([(n>>i & 1) for i in range(32)] )
        # num = 0
        # while n !=0:
        #     if (n-1)&1==1:
        #         ++num
        #     n=n>>1
        # return num