import sys
r = sys.stdin.readline

T = int(r())


for _ in range(T):
    n,m = map(int, r().split())
    dp = [[0 for _ in range(31)] for _ in range(31)]

    for i in range(1,31):
        dp[1][i] = i
    for i in range(2,n+1):
        for j in range(i,m+1):
            for k in range(j,i-1,-1):
                dp[i][j] += dp[i-1][k-1]

    print(dp[n][m])