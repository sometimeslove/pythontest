#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import  math
def huishufun(arr,x,y):
    if x>=y:
        return arr[x]
    middle = math.floor((x+y)/2)
    maxleft = huishufun(arr, x, middle)
    maxright = huishufun(arr, middle+1, y)
    maxmid = middleMax(arr, x, y )
    return max(maxleft,maxmid,maxright)

def middleMax(arr, x, y ):
    middle = math.floor((x+y)/2)
    maxleft = arr[middle]
    sumleft = arr[middle]
    maxright = arr[middle+1]
    sumright = arr[middle+1]
    for i in range(middle-1,x-1,-1):
        sumleft+=arr[i]
        if maxleft<sumleft+arr[i]:
            maxleft = sumleft
    for i in range(middle+2,y,1):
        sumright+=arr[i]
        if maxright<sumright+arr[i]:
            maxright = sumright
    return maxleft+maxright

if __name__ == '__main__':
    arr = [-1,-2,-4,5,-3,4,-1,-1]
    print(huishufun(arr,0,len(arr)-1))