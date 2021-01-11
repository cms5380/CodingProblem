import sys
from collections import deque

def bfs(left):
    while q:
        cur = q.popleft()

        for i in range(4):
            nx = cur[0] + dxy[i][0]
            ny = cur[1] + dxy[i][1]

            if 0 <= nx < H and 0 <= ny < W and visited[nx][ny] == 0:
                visited[nx][ny] = 1

                if field[nx][ny] == 1:
                    field[nx][ny] = 2
                    left -= 1
                else:
                    q.append([nx, ny])

    return left

dxy=[(1,0),(0,1),(-1,0),(0,-1)]

H, W = map(int, sys.stdin.readline().split(" "))
field = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(H)]

left = 0
for i in range(H):
    for j in range(W):
        if field[i][j] == 1:
            left += 1
            
q = deque()

cnt = 0
tmp = left

while left != 0:
    visited = [[0 for _ in range(W)] for _ in range(H)]
    q.append([0, 0])
    visited[0][0] = 1
    left = bfs(left)

    if left != 0:
        tmp = left

    cnt += 1
    for i in range(H):
        for j in range(W):
            if field[i][j] == 2:
                field[i][j] = 0

print(cnt)
print(tmp)