import sys

def dfs(start, cur, cnt, student, visit,first):
    if visit[cur]:
        if first[cur] != start:
            return 0
        
        return cnt - visit[cur]

    first[cur] = start
    visit[cur] = cnt
    return dfs(start, student[cur], cnt+1, student, visit, first)



T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    ans = 0
    student = [0] + list(map(int, sys.stdin.readline().split(" ")))
    first = [0 for _ in range(n+1)]
    visit = [0 for _ in range(n+1)]

    ans = 0
    for i in range(1,n+1):
        if not visit[i]:
            ans += dfs(i, i, 0, student, visit, first)

    print(ans)
