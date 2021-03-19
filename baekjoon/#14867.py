import sys
from collections import deque

a,b,c,d = map(int, sys.stdin.readline().split(' '))

def bfs():
    q = deque()
    q.append((0,0,0))
    visit = set()
    visit.add((0,0))
    while q:
        x,y,dep = q.popleft()

        if x == c and y == d:
            return dep
        
        nx, ny = a, y
        if (nx,ny) not in visit:
            q.append((nx,ny, dep+1))
            visit.add((nx,ny))

        nx, ny = x, b
        if (nx,ny) not in visit:
            q.append((nx,ny, dep+1))
            visit.add((nx,ny))

        nx, ny = 0, y
        if (nx,ny) not in visit:
            q.append((nx,ny, dep+1))
            visit.add((nx,ny))

        nx, ny = x, 0
        if (nx,ny) not in visit:
            q.append((nx,ny, dep+1))
            visit.add((nx,ny))

        nx, ny = 0 if x+y <= b else x+y-b, x+y if x+y <= b else b
        if (nx,ny) not in visit:
            q.append((nx,ny, dep+1))
            visit.add((nx,ny))

        nx, ny = x+y if x+y <= a else a, 0 if x+y <= a else x+y-a
        if (nx,ny) not in visit:
            q.append((nx,ny, dep+1))
            visit.add((nx,ny))
    return -1

print(bfs())