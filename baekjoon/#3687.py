import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
dp = [[0,float('inf')] for _ in range(101)]
dp[2][0] = 1
dp[3][0] = 7
dp[4][0] = 4
dp[5][0] = 5
dp[6][0] = 9
dp[7][0] = 8

dp[2][1] = 1
dp[3][1] = 7
dp[4][1] = 4
dp[5][1] = 2
dp[6][1] = 6
dp[7][1] = 8
nums = [1,7,4,2,0,8]
def find_max(idx,n):
    for i in range(idx,n+1):
        for j in range(2,i-1):
            dp[i][0] = max(int(str(dp[j][0]) + str(dp[i-j][0])), dp[i][0])
    return

def find_min(idx,n):
    for i in range(idx,n+1):
        for j in range(2,i-1):
            if 2<=i-j <8:
                dp[i][1] = min(int(str(dp[j][1]) + str(nums[i-j-2])), dp[i][1])
            else:
                dp[i][1] = min(int(str(dp[j][1]) + str(dp[i-j][1])), dp[i][1])
    return

answer = [[0,0] for _ in range(T)]
idx = 2
for i in range(T):
    n = int(input())
    if n > idx:
        find_max(idx, n)
        find_min(idx, n)
    
    dp[6][1] = 6
    answer[i][0] = dp[n][0]
    answer[i][1] = dp[n][1]
    idx = n

for i in range(T):
    print(answer[i][1], answer[i][0])