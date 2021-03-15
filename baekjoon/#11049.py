import sys

N = int(sys.stdin.readline())

matrix = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]

dp = [[0 for _ in range(N)] for _ in range(N)]

for k in range(1,N):
    for l in range(N-k):
        r = l + k
        dp[l][r] = float('inf')

        for i in range(l,r):
            dp[l][r] = min(dp[l][r], dp[l][i] + dp[i+1][r] + matrix[l][0] * matrix[i][1] * matrix[r][1])

print(dp[0][N-1])