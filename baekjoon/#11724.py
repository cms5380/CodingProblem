import sys
r = sys.stdin.readline

N, M = map(int, r().split())

parent = [i for i in range(N+1)]

def find(x):
    if parent[x] == x:
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x

for _ in range(M):
    a,b = map(int, r().split())
    if find(a) != find(b):
        union(a,b)

answer_set = set()

for p in parent:
    answer_set.add(find(p))

print(len(answer_set)-1)