import sys
from collections import deque


def dfs(x,y,cnt):
    global N, dp
    if dp[x][y] != 0:
        return dp[x][y]
    dp[x][y] = 1

    for dx, dy in ((0,1),(1,0),(-1,0),(0,-1)):
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < N:
            if maps[nx][ny] > maps[x][y]:
                dp[x][y] = max(dfs(nx,ny,cnt + 1) + 1, dp[x][y])

    return dp[x][y]

N = int(sys.stdin.readline())

maps = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(N):
        ans = max(ans,dfs(i,j,1))

print(ans)