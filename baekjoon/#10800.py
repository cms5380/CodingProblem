import sys

n = int(sys.stdin.readline())
ans = [0 for _ in range(n)]
player = []
for i in range(n):
    player.append(list(map(int, sys.stdin.readline().split(' '))) + [i])

player.sort(key=lambda x:x[1])

totalSum = 0
color = [0 for _ in range(n+1)]
j = 0
for i in range(len(player)):
    c,s,idx = player[i]

    while player[j][1] < player[i][1]:
        totalSum += player[j][1]
        color[player[j][0]] += player[j][1]
        j+=1

    ans[idx] = totalSum - color[c]

print(ans)