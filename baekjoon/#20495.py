import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
numn = []
numm = []
x = []
y = []
ans = []
for _ in range(N):
    a,b = map(int, input().split())
    x.append(a-b)
    y.append(a+b)

    numn.append(a-b)
    numm.append(a+b)

numn.sort()
numm.sort()

for i in range(N):
    l, r = 0, N - 1
    
    while l <= r:
        m = (l + r) // 2

        if x[i] >= numm[m]:
            l = m + 1
        else:
            r = m - 1

    start = l + 1

    l, r = 0, N - 1
    while l <= r:
        m = (l + r) // 2

        if y[i] >= numn[m]:
            l = m + 1
        else:
            r = m - 1

    end = r + 1
    print(start, end)