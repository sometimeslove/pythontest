# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        s = rotateArray[0]
        for i in range(1,len(rotateArray)):
            if s<=rotateArray[i]:
                s=rotateArray[i]
            else:
                return rotateArray[i]
        return s