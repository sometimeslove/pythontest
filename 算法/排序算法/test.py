import random
import numpy as np
from numpy.distutils.system_info import numpy_info

"""
快速排序
"""
def kuaisu(arr, left, right):
    if left >= right:
        return
    middle = patition(arr, left, right)
    kuaisu(arr, left, middle - 1)
    kuaisu(arr, middle + 1, right)


def patition(arr, left, right):
    flag = left
    for i in range(left + 1, right + 1):
        if arr[i] < arr[left]:
            arr[i], arr[flag] = arr[flag], arr[i]
            ++flag
    arr[left], arr[flag] = arr[flag], arr[left]
    return flag


if __name__ == '__main__':
    arr = np.random.randint(1, 100, 20)
    print(arr)
    l = len(arr) - 1
    kuaisu(arr, 0, l)
    print(arr)
    np.random.shuffle(arr)
    print(arr)
    kuaisu(arr, 0, l)
    print(arr)

