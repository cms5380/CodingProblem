import sys
input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))
nums.sort()
l,r = 0, N-1
ans = 0,2000000000

while l < r:
    res = nums[r] + nums[l]

    if res < 0:
        if abs(sum(ans)) > abs(res):
            ans = nums[l], nums[r]
        l += 1
    elif res > 0:
        if abs(sum(ans)) > abs(res):
            ans = nums[l], nums[r]
        r -= 1
    else:
        ans = nums[l], nums[r]
        break

print(ans[0], ans[1])

