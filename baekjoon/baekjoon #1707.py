# dxy = [(0,1),(1,0),(1,1)]

ans = 0
n = int(input())
arr = [list(map(int, input().split(' '))) for _ in range(n)]

def dfs(x, y, d):
    global ans
    if x == n-1 and y == n-1:
        ans += 1
        return

    if d == 0 or d == 1 or d == 2:
        if x + 1 < n and y + 1 < n:
            if arr[x+1][y] == 0 and arr[x][y+1] == 0 and arr[x+1][y+1] == 0:
                dfs(x+1, y+1, 2)

    if d == 0 or d == 2:
        if y + 1 < n:
            if arr[x][y+1] == 0:
                dfs(x, y+1, 0)

    if d == 1 or d == 2:
        if x + 1 < n:
            if arr[x+1][y] == 0:
                dfs(x+1, y, 1)

    


dfs(0,1,0)

print(ans)