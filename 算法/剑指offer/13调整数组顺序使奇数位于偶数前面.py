# -*- coding:utf-8 -*-
#标准答案解法
# # -*- coding:utf-8 -*-
# class Solution:
#     def reOrderArray(self, array):
#         # write code here
#         odd = [x for x in array if x%2]
#         even = [x for x in array if not (x%2)]
#         result = odd + even
#         return result
class Solution:
    def reOrderArray(self, array):
        arr1,arr2=[],[]
        for i in array:
            if int(i)%2==1:
                arr1.append(i)
            else:
                arr2.append(i)
        return arr1+arr2
if __name__=='__main__':
    try:
        S=Solution()
        array=input('请输入')
        print(S.reOrderArray( array))
    except:
        pass