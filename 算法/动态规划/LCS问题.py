#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def solution(x,y):
    if len(x)==0 or len(y)==0:
        return 0
    m = [[0 for i in range(len(y))]  for j in range(len(x))]
    for i in range(1,len(x)):
        for j in range(1,len(y)):
            if x[i]== y [j]:
                m[i][j] = m[i-1][j-1]+1
            else:
                m[i][j]= max (m[i-1][j],m[i][j-1])
    return m

def solution1 (a,b):
    d=[[0 for i in range(len(b)+1)] for j in range(len(a)+1)]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                d[i+1][j+1]= d[i][j]+1
            else:
                d[i+1][j+1] = max(d[i][j+1],d[i+1][j])
    return getelement(d,b)

def getelement(d,b):
    flag = d[-1][-1]
    r=[]
    for i in range(len(d)):
        if d[i][-1] == flag:
            r.append([b[j] for j in range(len(d[i])-1) if d[i][j]!=d[i][j+1]])
    return r

if __name__ == '__main__':
    x,y =['','a','b','c','d'],['','b','a','d','c']
    # lenx = input('请输入第一个序列的个数：\n')
    # for i in range(int(lenx)):
    #     x.append(input('第%d个：'%(i+1,)))
    # leny = input('请输入第二个序列的个数：\n')
    # for i in range(int(leny)):
    #     x.append(input('第%d个：'%(i+1,)))

    m = solution(x,y)
    print(m)
    n = solution1(x,y)
    print(n)