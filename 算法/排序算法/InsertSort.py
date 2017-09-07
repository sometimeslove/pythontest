#!/usr/bin/env python3
# -*- coding: utf-8 -*-
list = [12,32,76,23,89,78,45,32,45,47]
print(list)
def Insert_Sort(list):
    count = len(list)
    for i in range(1,count):
        k=list[i]
        j=i-1
        while (j>=0):
            if(list[j]<k):
                list[j+1]=list[j]
                list[j]=k
            j=j-1
            print(list)
Insert_Sort(list)