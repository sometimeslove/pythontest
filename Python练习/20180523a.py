#coding=utf-8
import sys
def solution (x,f,d,p):
    return (d+p*f)//(x+p)
for line in sys.stdin:
    a = [int(i) for i in line.split(',')]
    print(solution(a[0],a[1],a[2],a[3]))

