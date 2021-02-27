import sys
from collections import deque
def prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           
            for j in range(i+i, n, i): 
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]


def bfs(s, visit):
    global prime
    q = deque()
    
    visit[s] = 0

    q.append(s)

    while q:
        x = q.popleft()
        
        for i in range(4):
            x_s = str(x)
            for j in range(10):
                tmp = x_s[:i] + str(j) + x_s[i+1:]
                nxt = int(tmp)
                if nxt >= 1000 and nxt in prime and visit[nxt] == -1:
                    q.append(nxt)
                    visit[nxt] = visit[x] + 1

prime = prime_list(10000)


T = int(sys.stdin.readline())

for _ in range(T):
    s, e = map(int, sys.stdin.readline().split(" "))
    visit = [-1 for _ in range(10000)]
    bfs(s, visit)
    
    if visit[e] != -1:
        print(visit[e])
    else:
        print("Impossible")
