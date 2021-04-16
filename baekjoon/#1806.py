import sys
from heapq import heappop, heappush
from collections import deque
inp = sys.stdin.readline

n,s = map(int, inp().split())
nums = list(map(int, inp().split()))

i, j = 0, 0
ans = float('inf')
sumOfNum = 0
while i < n or j < n:
    if j == n and sumOfNum < s:
        break
    if sumOfNum >= s:
        sumOfNum -= nums[i]
        ans = ans if ans < j - i else j - i
        i += 1
    else:
        sumOfNum += nums[j]
        j += 1
    
print(ans)