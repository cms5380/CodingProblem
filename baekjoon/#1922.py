import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
parent = [i for i in range(N+1)]

def find_parent(x):
    if parent[x] == x:
        return x
    
    return find_parent(parent[x])

def union(x,y):
    x = find_parent(x)
    y = find_parent(y)

    if x != y:
        parent[x] = y
    



graph = []
for _ in range(M):
    a,b,c = map(int, input().split())
    graph.append([a, b, c])

graph.sort(key = lambda x : x[2])
answer = 0
for nxt in graph:
    a,b,c = nxt
    if find_parent(a) != find_parent(b):
        union(a,b)
        answer += c

print(answer)