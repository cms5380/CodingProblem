import sys
from collections import deque

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split(" ")))

S = 0
dp = [[0 for _ in range(21)] for _ in range(N-1)]

dp[0][nums[0]] = 1

for i in range(N-1):
    for j in range(21):
        if dp[i-1][j] != 0:
            if j - nums[i] >= 0:
                dp[i][j - nums[i]] += dp[i-1][j]

            if j + nums[i] <= 20:
                dp[i][j + nums[i]] += dp[i-1][j]


print(dp[-1][nums[-1]])
