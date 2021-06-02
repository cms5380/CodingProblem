import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    inp = list(map(int, input().split()))
    N = inp[0]
    money = inp[1:]
    S = 0
    money.sort()
    Sum = [0]

    for i in range(N):
        S += money[i]
        Sum.append(S)

    S = 0

    for i in range(2, N+1):
        mini = float('inf')
        for j in range(0,N - i + 1):
            r = j + i - 1 if j + i - 1 < N else N - 1
            tmp = money[r]
            candidate = tmp*i - (Sum[r+1] - Sum[j])
            mini = min(mini, candidate)
        S += mini
    print(S)