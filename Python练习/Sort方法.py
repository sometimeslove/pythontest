#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 假设我们用一组 tuple 表示学生名字和成绩：
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用 sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    t.lower
L2 = sorted(L, key=by_name)
print(L2)