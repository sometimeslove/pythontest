from itertools import chain

import numpy as np


def jishu(arr ):
    cur = [[] for i in range(10)]
    maxdept = get_depth(arr)
    for i in range (maxdept):
        for j in range (len(arr)):
            if arr[j]==0:
                cur[0].append(arr[j])
            index = (arr[j]//10**i)%10
            if index>0:
                cur[index].append(arr[j])
        arr= list(chain.from_iterable(cur))
        cur  = [[] for i in range(10)]
    return arr


def get_depth(arr):
    depth =0
    for i in range(len(arr)):
        if arr[i]//10**depth>0:
            depth+=1
    return depth

def calcute(value,seq):
    return (value//seq)%10

if __name__ == '__main__':
    arr = np.random.randint(1, 100, 20)
    print(arr)
    arr = jishu(arr)
    print(arr)
