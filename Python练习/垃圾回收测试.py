    n = int(input())
    for i in range(n):
        a,b,c = map(int,input().split())
        result = res(a,b,c)
        # if not result:
        #     return
        for j in result[:-1]:
            print(j,end=' ')
        print(result[-1])