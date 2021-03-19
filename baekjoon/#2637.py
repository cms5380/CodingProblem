import sys
from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
degree = [0 for _ in range(n+1)]
q = deque()
ans = [0 for _ in range(n+1)]

for _ in range(m):
    x,y,k = map(int, sys.stdin.readline().split(' '))
    graph[x].append((y,k))
    degree[y] += 1

for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)
        ans[i] = 1

for i in range(1, n + 1):
    x = q.popleft()
    
    for j in range(len(graph[x])):
        y, y_cost = graph[x][j]
        ans[y] += (y_cost * ans[x])
        degree[y] -= 1
        if degree[y] == 0:
            q.append(y)
for i in range(1,len(graph)):
    if len(graph[i]) == 0:
        print(i, ans[i])

