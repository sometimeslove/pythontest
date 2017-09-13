#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 利用递归函数计算阶乘
# N! = 1 * 2 * 3 * ... * N
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
#
# print('fact(1) =', fact(1))
# print('fact(5) =', fact(5))
# print('fact(10) =', fact(10))

def factA (n):
    return factB((n,1))

def factB(n,result):
    if(n==1):
        return result
    return factB(n-1,n*result)

print('factA(1) =', factA(1))
print('factA(5) =', factA(5))
print('factA(10) =', factA(4))

# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(4, 'A', 'B', 'C')