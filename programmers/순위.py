def solution(n, results):
    answer = 0
    graph = [[False for _ in range(n+1)] for _ in range(n+1)]
    for res in results:
        graph[res[0]][res[1]] = True
        
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
solution(8,[[1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [7, 8]])