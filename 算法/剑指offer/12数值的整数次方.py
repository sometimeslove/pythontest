# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        if exponent == -1:
            return pow(base,-1)
        return self.Power(base, exponent/2)*self.Power(base, exponent-exponent/2)