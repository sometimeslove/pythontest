#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def InsertSort(list):
    for i in range(1,len(list)):
        for j in range(i,0,-1):
            if(list[j-1]>list[j]):
                list[j-1],list[j]=list[j],list[j-1]
            else:
                break
    return
list= [21,6,79,54,76,34,12,34]
print(list)
list.reverse()
print(list)
InsertSort(list)
print(list)
