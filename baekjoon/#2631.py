# # O(N^2)
# # LIS 알고리즘(dp)

# import sys
# from collections import deque

# N = int(sys.stdin.readline())
# nums = [int(sys.stdin.readline()) for _ in range(N)]

# dp = [0 for _ in range(N)]

# dp[0]=1

# for i in range(1,N):
#     dp[i] = 1
#     for j in range(i):
#         if nums[j] < nums[i]:
#             dp[i] = max(dp[j] + 1, dp[i]) # j 번째까지 최장 증가 부분 수열에서 i번째 숫자를 추가한 것과 추가하지 않고 i 번째까지 중 더 큰 것

# print(N-max(dp))

# O(NlogN)
# LIS 알고리즘(이분탐색)

import sys
from collections import deque

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]
l = []
for num in nums:
    if len(l) == 0 or l[-1] < num:
        l.append(num)
    else:

        i = 0
        j = len(l) - 1

        while i < j:
            mid = (i + j) // 2

            if l[mid] < num:
                i = mid + 1
            else:
                j = mid
            

        l[j] = num

print(N - len(l))
        