import sys
from collections import deque

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
ans = []
dist = [0 for _ in range(N+1)]


def func(x):
    q = deque()
    q.append((x,0))
    visit = set()
    visit.add(x)
    while q:
        cur, dep = q.popleft()

        for nx in graph[cur]:
            if nx not in visit:
                q.append((nx,dep+1))
                dist[nx] = dep+1
                visit.add(nx)
    return

for _ in range(K):
    a,b = map(int, sys.stdin.readline().split(' '))
    graph[a].append(b)
    graph[b].append(a)
dicts = {}

for i in range(1, N+1):
    dist[i] = 1
    func(i)
    idx = -1
    maximum = 0
    for j in range(len(dist)):
        if dist[j] != 0:
            if idx == -1:
                idx = j
            maximum = maximum if maximum > dist[j] else dist[j]
    if idx not in dicts:
        dicts[idx] = (maximum,i)
    else:
        dicts[idx] = (maximum,i) if dicts[idx][0] > maximum else dicts[idx]

    
    dist = [0 for _ in range(N+1)]

print(len(dicts))
ans = list(dicts.values())
ans.sort(key=lambda x : x[1])

for a in ans:
    print(a[1])