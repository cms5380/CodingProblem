import sys
from heapq import heappop, heappush
def dij(start):
    pq = []
    dist[start] = 0
    heappush(pq, (0,start))
    while pq:
        cost, cur = heappop(pq)

        for i in range(len(graph[cur])):
            nxt, nxt_cost = graph[cur][i]

            if dist[nxt] > cost + nxt_cost:
                dist[nxt] = cost + nxt_cost
                heappush(pq, (dist[nxt], nxt))
    
    
N,M,X = map(int, sys.stdin.readline().split(' '))

graph = [[] for _ in range(N+1)]
dist = [float('inf') for _ in range(N+1)]
res = [0] * (N+1)


for _ in range(M):
    a, b, cost = map(int, sys.stdin.readline().split(' '))

    graph[a].append((b,cost))

for i in range(1,N+1):
    dist = [float('inf') for _ in range(N+1)]
    dij(i)
    res[i] = dist[X]
dist = [float('inf') for _ in range(N+1)]
dij(X)

for i in range(1,N+1):
    res[i] += dist[i]


print(max(res))