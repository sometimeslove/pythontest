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

if __name__ == '__main__':
    x,y =['','a','b','c'],['','b','a','d','c']
    # lenx = input('请输入第一个序列的个数：\n')
    # for i in range(int(lenx)):
    #     x.append(input('第%d个：'%(i+1,)))
    # leny = input('请输入第二个序列的个数：\n')
    # for i in range(int(leny)):
    #     x.append(input('第%d个：'%(i+1,)))

    m = solution(x,y)
    print(m)