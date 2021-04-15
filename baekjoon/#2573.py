import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visit = set()
cnt_island = 1

def yearGo(a,b):
    q = deque()
    q.append((a,b))
    visit.add((a,b))
    q1 = deque()
    while q:
        x,y = q.popleft()
        melt = 0

        for dx, dy in ((0,1), (1,0), (-1,0), (0,-1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if (nx,ny) not in visit and board[nx][ny] != 0:
                    visit.add((nx,ny))
                    q.append((nx,ny))
                if board[nx][ny] == 0:
                    melt += 1
        if melt > 0:
            q1.append((x,y,melt))

    while q1:
        x,y,cnt = q1.pop()
        if board[x][y] > cnt:
            board[x][y] -= cnt
        else:
            board[x][y] = 0

    return 1
ans = -1
while True:
    cnt_island = 0
    ans += 1
    flag = False
    
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0 and (i,j) not in visit:
                cnt_island += yearGo(i,j)
    
    if cnt_island == 0:
        ans = 0
        break
    elif cnt_island > 1:
        break
    visit = set()
print(ans)