import sys
from collections import deque

N = int(sys.stdin.readline())
height = list(map(int, sys.stdin.readline().split(' ')))

s = deque()

ans = []


for i in range(len(height)):
    h = height[i]
    while s:
        if h < s[0][1]:
            ans.append(s[0][0]+1)
            break
        s.popleft()

    if len(s) == 0:
        ans.append(0)

    s.appendleft((i,height[i]))

print(' '.join(map(str,ans)))