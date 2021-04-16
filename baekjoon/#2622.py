import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
candidates = set()
for i in range(1,(n//3) + 1):
    for j in range(i, n):
        k = n - i - j
        if j > k: break
        if i + j > k: candidates.add((i,j,k))

print(len(candidates))