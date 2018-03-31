# 有一楼梯共M级，刚开始时你在第一级，若每次只能跨上一级或二级，要走上第M级，共有多少种走法？
# Sample Input
# 2
# 3
# Sample Output
# 1
# 2
def solution(start , end):
    if end <= start:
        return 0
    if end-1 == start or end-2 == start:
        return 1
    return solution(start,end-1)+solution(start,end-2)+1
def solution1(start ,end):
    if end <=start:
        return 0
    s=0
    for i in range(end-1,start,-1):
        s=s+solution1(start,i)+1
    return s
if __name__ == '__main__':
    print(solution(1,5))
    print(solution1(1,5))