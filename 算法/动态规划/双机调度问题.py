#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 问题：独立任务最优调度，又称双机调度问题：用两台处理机A和B处理n个作业。设第i个作业交给机器A处理时所需要的时间是a[i]，若由机器B来处理，则所需要的时间是b[i]。现在要求每个作业只能由一台机器处理，每台机器都不能同时处理两个作业。设计一个动态规划算法，使得这两台机器处理完这n个作业的时间最短（从任何一台机器开工到最后一台机器停工的总的时间）。
# 研究一个实例：
# n=6
# a = {2, 5, 7, 10, 5, 2};
# b = {3, 8, 4, 11, 3, 4}.
def solution():
    a = [0, 2, 5, 7, 10, 5, 2]
    b = [0, 3, 8, 4, 11, 3, 4]
    pa,pb = [0],[0]
    la,lb=[],[]
    for i in range(1,len(a)):
        if a[i]+pa[len(pa)-1]>b[i]+pb[len(pb)-1]:
            pb.append(b[i]+pb[len(pb)-1])
            lb.append(i)
        else:
            pa.append(a[i]+pa[len(pa)-1])
            la.append(i)
    return max(pa[len(pa)-1],pb[len(pb)-1]),la,lb
if __name__ == '__main__':
    print(solution())