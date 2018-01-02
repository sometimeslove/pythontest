#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  问题描述:
#  设I是一个n位十进制整数，如果将I划分为k段，则可得到k个整数，这k个整数
#  的乘积称为I的一个K乘积，试设计一个算法，对于给定的I和K，求出I的最大乘积
from functools import reduce
def CountSum(n):
    p = [3,2,0,5,7,8,6,4]
    s = [0,0,0,0,0,0,0,0]
    for i in range(len(p)):
        for j in range(n):
            tmp = GetValue(p,j+1,i)
            if s[i]<s[j]*tmp:
                s[i]=s[j]*tmp
    return s
def GetValue(s,i,j):
    if i==j:
        return s[i]
    else:
        return reduce(lambda x,y:x*10+y,s[i:j+1])
if __name__=='__main__':
    try:
        test =CountSum(7)
        print(test)
    except:
        pass