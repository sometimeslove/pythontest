import sys
def Solution(n,price,cost):
    maxcost = max(cost)
    goodV = [0 for x in range(n+1)]
    for i in range(1, n+1):
        for j in range(1,len(cost)):
            if i<cost[j]:
                continue
            if (price[j]+ goodV[i-cost[j]])>goodV[i]:
                goodV[i] = price[j]+ goodV[i-cost[j]]
    return goodV[n]

if __name__ == '__main__':
    #利润
    price = [0]
    #本钱
    cost = [0]
    tmp = list(map(int, sys.stdin.readline().strip().split(' ')))
    for i in range(tmp[0]):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split(' ')))
        price.append(values[1]-values[0])
        cost.append(values[0])
    print(Solution(tmp[1],price,cost))