import sys
from collections import *
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x,y = map(int, input().split())
    dist = y - x
    ans = 0

    tmp = 1
    S = 0
    while S < dist:
        ans += 1
        S += tmp
        if ans % 2 == 0:
            tmp += 1

    print(ans)