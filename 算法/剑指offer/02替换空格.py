#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import string
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        ret = []
        for str in s:
            if str.isspace():
                ret.append('%20')
            else:
                ret.append(str)
        return ''.join(ret)



if __name__=='__main__':
    try:
        S=Solution()
        array=input('请输入')
        print(S.replaceSpace( array))
    except:
        pass