import sys

def find_(x):
    if parent[x] == x:
        return x

    return find_(parent[x])

def union_(a,b):
    a = find_(a)
    b = find_(b)

    if a != b:
        parent[a] = b

def solution():
    for i in range(1,n+1):
        for j, k in enumerate(list(map(int, sys.stdin.readline().split(' ')))):
            if k == 1:
                union_(i,j+1)

    order = list(map(int, sys.stdin.readline().split(' ')))

    tmp = find_(order[0])
    flag = True
    for i in range(1, len(order)):

        if find_(order[i]) != tmp:
            flag = False
            break

    if flag:
        return "YES"
    else:
        return "NO"

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

parent = [i for i in range(n+1)]

print(solution())