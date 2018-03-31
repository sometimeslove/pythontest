# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        if number<0:
            return 0
        s = [0 for i in range(number+1)]
        s[0],s[1]=1 ,1
        for i in range(2,number+1):
            s[i] = sum(s)
        return s[number]
if __name__=='__main__':
    try:
        S=Solution()
        print(S.jumpFloorII( 2))
    except:
        pass