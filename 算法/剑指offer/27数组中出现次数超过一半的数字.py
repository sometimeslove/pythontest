# -*- coding:utf-8 -*-
import collections
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if numbers is None:
            return 0
        max=numbers[0]
        count = 0
        for i in numbers:
            if max == i:
                count+=1
            else:
                count-=1
                if count<0:
                    max = i
                    count = 1

        if collections.Counter(numbers)[max]>len(numbers)/2:
            return max
        else:
            return  0