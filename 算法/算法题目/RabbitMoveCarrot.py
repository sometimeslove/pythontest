#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#一只小兔子有100根胡萝卜, 它要走50米才能到家, 每次它最多搬50根胡萝卜, 而每走1米就要吃掉1根胡萝卜, 请问它最多能把多少根胡萝卜搬到家里?
"""
一旦折返, 折返的路程上花费为 3c/m; 不折返的话花费为 1c/m.
因此需要尽量减小折返, 确保最后不折返的时候带的萝卜尽量多(上限50个).
假设总折返距离为 x(m), 有 100 - 3x <= 50, 即 x >= 50 / 3
最后剩下的萝卜个数为: (100 - 3x) - (50 - x) = 50 - 2x <= 50 / 3
因此, 至多剩下 16 个萝卜(只能取整数的话), 此时折返路程为 17m.
能取分数的话直接取等号就行了, 不再赘述.
"""
distance = 50
maxTake = 50
carrot_count = 100
def MaxCount(carrot_count,maxTake,distance):
    max_count = 0
    for i in range(0,distance):
        last_count= carrot_count % maxTake
        carrot_count = carrot_count - 2 * int(carrot_count / maxTake)-last_count
        if(last_count>2):
            carrot_count=carrot_count+last_count-1
        else:
            carrot_count=carrot_count+1
    return carrot_count

value = MaxCount(carrot_count,maxTake,distance)
print(value)


