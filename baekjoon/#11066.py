import sys

T = int(sys.stdin.readline())

for _ in range(T):
    K = int(sys.stdin.readline())
    disk = [0]+list(map(int, sys.stdin.readline().split(' ')))
    dp = [[0 for _ in range(K+1)] for _ in range(K+1)]
    S = [0] * (K+1)
    for i in range(1,K+1):
        S[i] = S[i-1] + disk[i]

    for i in range(1,K):
        for start in range(1,K-i+1):
            end = start + i
            dp[start][end] = float('inf')

            for m in range(start, end):
                dp[start][end] = min(dp[start][end], dp[start][m] + dp[m+1][end] + S[end] - S[start-1])

    print(dp[1][K])
