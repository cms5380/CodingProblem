import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
operater = list(map(int, input().split()))
mini, maxi = float('inf'), -float('inf')
def dfs(res, idx):
    global mini, maxi
    if idx == N:
        mini = mini if mini < res else res
        maxi = maxi if maxi > res else res
        return

    if operater[0] > 0:
        operater[0] -= 1
        dfs(res+nums[idx], idx+1)
        operater[0] += 1
    if operater[1] > 0:
        operater[1] -= 1
        dfs(res-nums[idx], idx+1)
        operater[1] += 1
    if operater[2] > 0:
        operater[2] -= 1
        dfs(res*nums[idx], idx+1)
        operater[2] += 1
    if operater[3] > 0:
        operater[3] -= 1
        dfs(int(res/nums[idx]), idx+1)
        operater[3] += 1

dfs(nums[0],1)

print(maxi,mini)