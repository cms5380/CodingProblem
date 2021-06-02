import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

l,r = 0,0

ans = 0

Up = 1
Down = 1

for i in range(N-1):
    if nums[i] > nums[i+1]:
        Down += 1
        Up = 1
    elif nums[i] < nums[i+1]:
        Up += 1
        Down = 1
    else:
        Up += 1
        Down += 1
    
    if Up > 2 or Down > 2:
        ans = ans if ans > i + 1 - l else i + 1 - l
        l = i
        if Up == 3: Up -= 1
        if Down == 3: Down -= 1

    if i == N - 2:
        ans = ans if ans > i + 2 - l else i + 2 - l

print(ans)