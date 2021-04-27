import sys
from heapq import *
input = sys.stdin.readline

N = int(input())
maxHeap = []

for _ in range(N):
    x = int(input())
    if x == 0 and len(maxHeap) > 0:
        print(heappop(maxHeap)[1])
    elif x == 0 and len(maxHeap) == 0:
        print(0)
    else:
        heappush(maxHeap, (-x,x))
    