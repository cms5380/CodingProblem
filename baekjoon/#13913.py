from collections import deque
visited = set()
def bfs(start, end):
    q=deque()
    q.append([start,[start]])
    visited.add(0)
    while q:
        cur, path = q.popleft()

        if cur == end:
            return [len(path) - 1,path]

        if cur + 1 <= 100000 and cur + 1 not in visited:
                q.append([cur+1,path+[cur+1]])
                visited.add(cur+1)
        if cur - 1 >= 0 and cur - 1 not in visited:
                q.append([cur-1,path+[cur-1]])
                visited.add(cur-1)
        if cur * 2 <= 100000 and cur * 2 not in visited:
                q.append([cur*2,path+[cur*2]])
                visited.add(cur*2)

n, k = map(int, input().split())
if n > k:
    ans=0
    for i in range(n,k-1,-1):
       ans += 1
       print(i, end=' ')
    print(ans)
else:
    ans = bfs(n,k)
    print(ans[0])
    for num in ans[1]:
        print(num, end=" ")