import sys

def sol(T, P):
    dp = [0] * (N + 1)
    cur_max = 0

    for i in range(N):
        if i + T[i] <= N:
            dp[i + T[i]] = max(dp[i] + P[i], dp[i + T[i]])
            cur_max = max(cur_max, dp[i + T[i]])

        dp[i+1]=max(dp[i+1], dp[i])
        cur_max = max(cur_max, dp[i + 1])
            
    return dp[-1]

N = int(sys.stdin.readline())
T = []
P = []

for _ in range(N):
    a,b = map(int, sys.stdin.readline().split(' '))
    T.append(a)
    P.append(b)

print(sol(T,P))
