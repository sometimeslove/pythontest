#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 问题描述：
#        一家公司购买长钢条，将其切割成短钢条出售，切割本身没有成本，
#        长度为i的短钢条的价格为Pi。那给定一段长度为n的钢条和一个价格表Pi,求钢条的切割方案使得收益Rn最大。如一个Pi如下：
# 长度i   	1	2	3	4	5	6	7	8	9	10
# 价格Pi	1	5	8	9	10	17	17	20	24	30
# 在距离钢条左端i长度处，我们总是可以选择切割或者不切割，所以长度为n的钢条共有2的n-1次方中不同的切割方案.
def Solution(n):
    price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    # singlePrice = [p/len for len,p in enumerate(price)]
    # 获取一个单价的字典，并将这个字典按照降序进行排序
    # singlePrice = sorted(dict(zip([x for x in range(len(price))],price)), reverse=True)
    goodV = [0 for x in range(n+1)]
    eachL = [0 for x in range(n+1)]
    for i in range(1, n+1):
        for j in range(1,min(i+1,len(price))):
            if (price[j]+ goodV[i-j])>goodV[i]:
                goodV[i] = price[j]+ goodV[i-j]
                eachL[i] = j
    ret = getEachLengh(eachL)
    return goodV[n],ret

def getEachLengh(eachL):
    ret = []
    flag = len(eachL)-1
    while flag > 0:
        ret.append(eachL[flag])
        flag -= eachL[flag]
    return ret
if __name__ == '__main__':
    # print(Solution(15)[1])
    print(Solution(15))