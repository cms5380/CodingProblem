import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split(' ')))
dp = [1 for _ in range(n)]
reverse_dp = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

arr=arr[::-1]
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i] and reverse_dp[i] < reverse_dp[j] + 1:
            reverse_dp[i] = reverse_dp[j] + 1
reverse_dp=reverse_dp[::-1]

ans = 0
for i in range(n):
    ans = ans if ans > dp[i] + reverse_dp[i] - 1 else dp[i] + reverse_dp[i] - 1

print(ans)