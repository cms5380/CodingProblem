import sys
import copy
from collections import deque


def bfs(a,b, idx):
    q = deque()
    q.append((a,b))
    newboard[a][b] = idx
    while q:
        x, y = q.popleft()

        for dx,dy in ((0,1),(1,0),(-1,0),(0,-1)):
            nx, ny = x + dx, y + dy

            if 0<=nx<N and 0<=ny<N:
                if (nx,ny) not in visit and board[nx][ny]:
                    newboard[nx][ny] = idx
                    q.append((nx,ny))
                    visit.add((nx,ny))

    return

def bfs1(a,b, num):
    q = deque()
    q.append((a,b,0))
    visited = set()
    visited.add((a,b))
    while q:
        x, y, dep = q.popleft()
        if newboard[x][y] != 0 and newboard[x][y] != num:
            return dep
        for dx,dy in ((0,1),(1,0),(-1,0),(0,-1)):
            nx, ny = x + dx, y + dy

            if 0<=nx<N and 0<=ny<N:
                if newboard[nx][ny] != num and (nx,ny) not in visited:
                    q.append((nx,ny, dep + 1))
                    visited.add((nx,ny))
    return float('inf')
N = int(sys.stdin.readline())

board = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]
newboard = copy.deepcopy(board)
idx = 1
visit = set()
for i in range(N):
    for j in range(N):
        if (i,j) not in visit and board[i][j]:
            bfs(i,j, idx)
            visit.add((i,j))
            idx += 1

ans = float('inf')
for i in range(N):
    for j in range(N):
        if board[i][j]:
            ans = min(ans,bfs1(i,j,newboard[i][j]))
print(ans)