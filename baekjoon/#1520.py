import sys
sys.setrecursionlimit(10**6)
dxy = [(0,1),(1,0),(-1,0),(0,-1)]

def dfs(x,y):
    if x == M - 1 and y == N - 1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0

    for dx,dy in dxy:
        nx, ny = dx + x, dy + y

        if 0 <= nx < M and 0 <= ny < N:
            if board[x][y] > board[nx][ny]:
                dp[x][y] += dfs(nx,ny)
    
    return dp[x][y]

M, N = map(int, sys.stdin.readline().split(" "))
board = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)]


print(dfs(0,0))
