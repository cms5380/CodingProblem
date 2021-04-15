import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
board = [['' for _ in range(M)] for _ in range(N)]
visit = [[float('inf') for _ in range(M)] for _ in range(N)]
def bfs(a,b):
    q = deque()
    
    q.append([a,b])
    visit[a][b] = 0
    while q:
        x, y = q.popleft()
                
        for dx, dy in ((0,1), (1,0), (-1,0), (0,-1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == '1':
                    if visit[nx][ny] > visit[x][y] + 1:
                        visit[nx][ny] = visit[x][y] + 1
                else:
                    if visit[nx][ny] > visit[x][y]:
                        visit[nx][ny] = visit[x][y]
                q.append([nx,ny])


for i in range(N):
    tmp = list(input().strip())
    for j, c in enumerate(tmp):
        board[i][j] = c

bfs(0,0)
print(visit[-1][-1])