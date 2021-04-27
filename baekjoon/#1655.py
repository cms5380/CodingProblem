import sys
from heapq import *
input = sys.stdin.readline

N = int(input())

minHeap = []
maxHeap = []

for _ in range(N):
    x = int(input())
    if len(minHeap) == len(maxHeap):
        heappush(minHeap, (-x, x))
    else:
        heappush(maxHeap, x)

    if len(maxHeap) > 0 and minHeap[0][1] > maxHeap[0]:
        a = heappop(minHeap)[1]
        b = heappop(maxHeap)

        heappush(minHeap, (-b,b))
        heappush(maxHeap, a)

    
    
    print(minHeap[0][1])