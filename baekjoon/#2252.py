import sys
from collections import deque
r = sys.stdin.readline
n,m = map(int, r().split())
q = deque()
depth = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
ans = []


for _ in range(m):
    a ,b = map(int, r().split())

    graph[a].append(b)
    depth[b] += 1


for i in range(1,n+1):
    if depth[i] == 0:
        q.append(i)

for i in range(1,n+1):
    if len(q) == 0:
        break

    x = q.popleft()

    ans.append(x)

    for j in range(len(graph[x])):
        y = graph[x][j]
        depth[y] -= 1

        if depth[y] == 0:
            q.append(y)

print(' '.join(map(str,ans)))
