#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def CountSum(n):
    p = [3,2,5,7,8,6,4]
    s = [0,0,30]
    for i in range(3,n):
        s.append(min((s[i-1]+p[0]*p[i-1]*p[i]),(s[i-3]+p[0]*p[i-2]*p[i]+p[i-2]*p[i-1]*p[i])))
    return s
if __name__=='__main__':
    try:
        test =CountSum(7)
        print(test)
    except:
        pass