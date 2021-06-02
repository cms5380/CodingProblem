import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int, input().split())
path = list(map(int, input().split()))

cost = [list(map(int,input().split())) for _ in range(N-1)]
cnt = [0 for _ in range(N)] 
for i in range(1,M):
    s,e=path[i-1], path[i]
    if s > e:
        s, e = e, s
    
    cnt[s-1] += 1
    cnt[e-1] -= 1

ans = 0
S = 0

for i in range(N):
    S += cnt[i]
    ans += min(S * cost[i][0], S * cost[i][1] + cost[i][2])

print(ans)


