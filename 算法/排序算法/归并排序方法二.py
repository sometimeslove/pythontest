# -*- coding: utf-8 -*-
"""归并排序"""
import random

def merge(left, right):
    """合并两个数组"""
    merged = []
    # i, j 分别作为left和right的下标
    i, j = 0, 0
    # 同样的原理，两种不同的写法
    # left_len, right_len = len(left), len(right)
    # while i < left_len and j < right_len:
    #     if left[i] <= right[j]:
    #         merged.append(left[i])
    #         i += 1
    #     else:
    #         merged.append(right[j])
    #         j += 1
    # merged.extend(left[i:])
    # merged.extend(right[j:])
    while len(right)>0 and len(left)>0:
        if left[i] <= right[j]:
            merged.append(left.pop(i))
        else:
            merged.append(right.pop(j))
    merged.extend(left)
    merged.extend(right)
    return merged


def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge(left, right)


if __name__ == '__main__':
    lst = []
    for i in range(30):
        lst.append(random.randint(1, 100))
    print (lst)
    result = merge_sort(lst)
    print (result)
