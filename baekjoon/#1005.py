import sys
from collections import deque
T = int(sys.stdin.readline())

def topological_sort(N,K):
    time = [0] + list(map(int, sys.stdin.readline().split(' ')))

    order = [[] for _ in range(N+1)]
    degree = [0 for _ in range(N+1)]
    for _ in range(K):
        x,y = map(int, sys.stdin.readline().split(' '))

        order[x].append(y)
        degree[y] += 1

    q = deque()
    
    for i in range(1, N+1):
        if degree[i] == 0:
            q.append(i)
    ret = [0 for _ in range(N+1)]
    for i in range(1,N+1):
        build = q.popleft()
        


        for j in range(len(order[build])):
            nxt = order[build][j]
            degree[nxt] -= 1
            ret[nxt] = max(time[build] + ret[build], ret[nxt])
            if degree[nxt] == 0:
                q.append(nxt)
                

    win = int(sys.stdin.readline())
    return ret[win] + time[win]
    
while T > 0:
    N, K = map(int, sys.stdin.readline().split(' '))
    
    print(topological_sort(N,K))
    T -= 1