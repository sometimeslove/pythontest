#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import random
def mergesort(list,beginindex,middleindex,endindex):
    list1=list[beginindex:middleindex+1]
    list2=list[middleindex+1:endindex+1]
    j,k=0,0
    lenA,lenB=middleindex-beginindex+1,endindex-middleindex
    for i in range(beginindex,endindex+1):
        if(j>=lenA):
            for m in range(i,endindex+1):
                list[m]=list2[k]
                k=k+1
            break
        if(k>=lenB):
            for n in range(i,endindex+1):
                list[n]=list1[j]
                j=j+1
            break
        if(list1[j]>list2[k]):
            list[i] = list2[k]
            k +=1
        else:
            list[i] = list1[j]
            j +=1
        print(list[i])
def merge(list,p,q):
    if(p<q):
        r=math.floor((p+q)/2)
        merge(list,p,r)
        merge(list,r+1,q)
        mergesort(list,p,r,q)
if __name__ == '__main__':
    list = []
    for i in range(30):
        list.append(random.randint(1, 100))
    print(list)
    merge(list,0,len(list)-1)
    print(list)

