from collections import deque
f,s,g,u,d = map(int, input().split())

def bfs():
    q = deque()
    q.append((s,0))
    visit = set()
    visit.add(s)

    while q:
        x, dep = q.popleft()

        if x == g:
            return dep

        for dx in (u,-d):
            nx = x + dx

            if nx not in visit and 0 < nx <= 1000000:
                q.append((nx, dep + 1))
                visit.add(nx)
    return -1
    
ans = bfs()
print(ans if ans != -1 else "use the stairs")