def solution(a):
    d = [[0 for i in range(len(a))] for j in range(len(a))]
    for m in range(1,len(a)):
        for n in range(0,len(a)-m):
            if a[n]==a[n+m]:
                d[n][n+m] = d[n+1][n+m-1]
            else:
                d[n][n+m] = min(d[n][n+m-1],d[n+1][n+m])+1
    return d

if __name__ == '__main__':
    a = 'wsmfswa'
    print(solution(a))