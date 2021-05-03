import sys
r = sys.stdin.readline
n,m = map(int, r().split())
graph = [[False for _ in range(n+1)] for _ in range(n+1)]

def solution():
    answer = 0
    

    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = True

    for i in range(1,n+1):
        cnt = 0
        for j in range(1,n+1):
            if graph[i][j] or graph[j][i]:
                cnt += 1
        if cnt == n - 1:
            answer+=1


    return answer

    
for _ in range(m):
    a ,b = map(int, r().split())
    graph[a][b] = True




print(solution())
