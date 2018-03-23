#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# http://acm.hdu.edu.cn/showproblem.php?pid=2084
def solution(a):
    d=a
    for i in range(1,len(a)):
        for j in range(1,i+2):
            tmp1 = d[i-1][j]+a[i][j]
            tmp2 = d[i-1][j-1]+a[i][j]
            if tmp1>tmp2:
                d[i][j] = tmp1
            else:
                d[i][j] = tmp2
    return max(d[len(d)-1])
if __name__ == '__main__':
    a = [[0,7,0,0,0,0],[0,3,8,0,0,0],[0,8,1,0,0,0],[0,2,7,4,4,0],[0,4,5,2,6,5]]
    print(solution(a))