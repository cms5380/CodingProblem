# import sys
# r = sys.stdin.readline
# n,m = map(int, r().split())
# parent = [i for i in range(n+1)]

# def union(x,y):
#     parent_x = find(x)
#     parent_y = find(y)

#     if parent_x != parent_y:
#         parent[y] = x
        

# def find(x):
#     if parent[x] == x:
#         return x
#     parent[x] = find(parent[x])
#     return parent[x]

# for _ in range(m):
#     a,b,c = map(int, r().split())
#     if a == 0:
#         union(b,c)
#     else:
#         if find(b) == find(c):
#             print("YES")
#         else:
#             print("NO")

n,m = map(int, input().split(' '))

def find(x, parent):
    if x == parent[x]:
        return x
    
    p = find(parent[x], parent)
    parent[x] = p
    return p

def union(a,b,parent):
    a = find(a,parent)
    b = find(b,parent)

    if a!=b:
        parent[b] = a
parent = [i for i in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split(' '))

    if a == 0:
        union(b,c,parent)
    else:
        if find(b,parent) != find(c,parent):
            print('NO')
        else:
            print('YES')