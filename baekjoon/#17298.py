from collections import deque

n = int(input())

nums = list(map(int, input().split()))
s = deque()
ans = [-1 for _ in range(n)]
for i, num in enumerate(nums):
    while s and nums[s[-1]] < num:
        ans[s.pop()] = num
        
    s.append(i)

for i in ans:
    print(i)