# http://acm.hdu.edu.cn/showproblem.php?pid=2044
def solution (start,end):
    if start==end-1 or start == end-2:
        return 1
    return solution(start,end-1)+solution(start,end-2)+1
if __name__ == '__main__':
    print(solution(3,6))