import sys
from heapq import heappop, heappush
from collections import deque
input = sys.stdin.readline

n,e = map(int, input().split())
graph = [[] for _ in range(n+1)]

def dij(start):
    q = []
    dist = [float('inf') for _ in range(n+1)]
    heappush(q, start)
    dist[start] = 0

    while q:
        cur = heappop(q)
    
        for nxtNode, nxtCost in graph[cur]:
            if dist[nxtNode] > dist[cur] + nxtCost:
                dist[nxtNode] = dist[cur] + nxtCost
                heappush(q, nxtNode)
    return dist
for _ in range(e):
    a,b,c = map(int, input().split())

    graph[a].append([b,c])
    graph[b].append([a,c])


v1, v2 = map(int, input().split())


startDist = dij(1)
v1Dist = dij(v1)
v2Dist = dij(v2)
candidate1 = startDist[v1] + v1Dist[v2] + v2Dist[n]
candidate2 = startDist[v2] + v2Dist[v1] + v1Dist[n]

if candidate1 == float('inf') and candidate2 == float('inf'):
    print(-1)
else: print(candidate1) if candidate1 < candidate2 else print(candidate2)


