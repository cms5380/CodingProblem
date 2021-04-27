import sys
from heapq import *
input = sys.stdin.readline

N, K = map(int, input().split())
jewel = []
bags = []

for _ in range(N):
    heappush(jewel, list(map(int, input().split())))

for _ in range(K):
    heappush(bags, int(input()))

ans = []
answer = 0
while len(bags) > 0:
    bag = heappop(bags)
    while len(jewel) > 0:
        if jewel[0][0] <= bag:
            heappush(ans, -jewel[0][1])
            heappop(jewel)
        else: break

    if len(ans) > 0:
        answer += -heappop(ans)
print(answer)