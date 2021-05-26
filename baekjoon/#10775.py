import sys
from collections import deque
r = sys.stdin.readline

def find(x):
    if airport[x] == x:
        return x
    
    airport[x] = find(airport[x])
    return airport[x]

def union(a,b):
    a = find(a)
    b = find(b)

    if a!=b:
        airport[a] = b

G = int(r())
P = int(r())

airport = [i for i in range(G+1)]
answer = 0
for _ in range(P):
    g = int(r())

    docking = find(g)
    if docking != 0:
        union(docking, docking -1)
        answer += 1
    else:
        break

print(answer)
