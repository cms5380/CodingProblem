import sys
sys.setrecursionlimit(10**9)
graph = []
visit = []
def dfs(cur, flag):
    visit[cur] = flag

    for nx in graph[cur]:
        if visit[nx] == 0:
            visit[nx] = -flag
            dfs(nx, -flag)
            
def isBipartite():
    for i in range(1,len(graph)):
        for nxt in graph[i]:
            if visit[nxt] == visit[i]:
                return False
    return True
Tcase = int(sys.stdin.readline())

for case in range(Tcase):
    V, E = map(int, sys.stdin.readline().split(' '))
    visit = [0 for _ in range(V+1)]
    graph = [[] for _ in range(V + 1)]
    for i in range(E):
        a,b = map(int, sys.stdin.readline().split(' '))
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V+1):
        if visit[i] == 0:
             dfs(i,1)

    if isBipartite():
        print("YES")
    else: print("NO")

    