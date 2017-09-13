#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 如果 list 中既包含字符串，又包含整数，由于非字符串类型没有 lower()
def test():
    list = ['Hello', 55, True, 'World']
    l = [i.lower() for i in list if isinstance(i, str) ]
    return l
a=test()
print(a)