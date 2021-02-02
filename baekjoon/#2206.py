import sys
from collections import deque

dxy = [(0,1),(1,0),(-1,0),(0,-1)]

N, M = map(int, sys.stdin.readline().split(" "))
visit = [[[0]*3 for _ in range(M)] for _ in range(N)]

board = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]


def BFS():
    q = deque()
    q.append((0,0,0,1))

    visit[0][0][0] = True

    while q:
        x, y, break_block, dep = q.popleft()

        if x == N-1 and y == M-1:
            print(dep)
            return

        for dx,dy in dxy:
            nx, ny = dx + x, dy + y
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny]==1 and break_block == 0:
                    visit[nx][ny][break_block+1] = True
                    q.append((nx,ny,break_block+1,dep+1))
                elif board[nx][ny] == 0 and visit[nx][ny][break_block] == False:
                    visit[nx][ny][break_block] = True
                    q.append((nx,ny,break_block,dep+1))
    print(-1)
    return 

BFS()