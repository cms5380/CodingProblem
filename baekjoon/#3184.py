import sys
from collections import deque
r = sys.stdin.readline

R, C = map(int, r().split())
maps = [list(r().strip()) for _ in range(R)]
visited = set()

def bfs(a,b):
    visited.add((a,b))
    q = deque()
    q.append((a,b))
    wolf = 0
    sheep = 0
    if maps[a][b] == 'v':
        wolf += 1
    elif maps[a][b] == 'o':
        sheep += 1
        
    while q:
        x,y = q.popleft()
        
        for dx, dy in ((0,1),(1,0),(-1,0),(0,-1)):
            nx, ny = dx + x, dy + y

            if 0 <= nx < R and 0 <= ny < C:
                if (nx,ny) not in visited and maps[nx][ny] != '#':
                    if maps[nx][ny] == 'v':
                        wolf += 1
                    elif maps[nx][ny] == 'o':
                        sheep += 1
                    q.append((nx,ny))
                    visited.add((nx,ny))


    if sheep > wolf:
        return (sheep, 0)
    else:
        return (0, wolf)

ans_s, ans_w = 0, 0
for i in range(R):
    for j in range(C):
        if maps[i][j] != '#' and (i,j) not in visited:
            tmp = bfs(i,j)
            ans_s += tmp[0]
            ans_w += tmp[1]
    
print(ans_s, ans_w)

