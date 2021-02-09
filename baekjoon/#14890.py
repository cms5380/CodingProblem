import sys

n, l = map(int, sys.stdin.readline().split(' '))

maps = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]
ans = 0

j = 0

for i in range(n):
    cnt = 1
    flag = True
    for j in range(0,n-1):
        if maps[i][j] == maps[i][j+1]:
             cnt += 1
        elif maps[i][j] == maps[i][j+1] - 1 and cnt >= l:
             cnt = 1
        elif maps[i][j] == maps[i][j+1] + 1 and cnt >= 0:
             cnt = -l + 1
        else: 
            flag = False
            break
    
    if j == n - 2 and cnt >= 0 and flag:
         ans += 1

for i in range(n):
    cnt = 1
    flag = True

    for j in range(0,n-1):
        if maps[j][i] == maps[j+1][i]:
             cnt += 1
        elif maps[j][i] == maps[j+1][i] - 1 and cnt >= l:
             cnt = 1
        elif maps[j][i] == maps[j+1][i] + 1 and cnt >= 0:
             cnt = -l + 1
        else: 
            flag = False
            break
    
    if j == n - 2 and cnt >= 0 and flag:
         ans += 1

print(ans)