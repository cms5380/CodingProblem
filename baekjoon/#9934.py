import sys
from collections import *
input = sys.stdin.readline

k = int(input())
num = list(map(int, input().split()))

ans = [[] for _ in range(k)]
def func(l,r, level):
    m = (l+r)//2
    ans[level].append(num[m])
    
    if l == r:
        return

    func(l, m - 1, level + 1)
    func(m + 1, r, level + 1)

func(0, len(num)-1, 0)

for i in range(k):
    print(' '.join(map(str, ans[i])))
