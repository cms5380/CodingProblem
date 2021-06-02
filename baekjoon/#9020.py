import sys
from collections import *
input = sys.stdin.readline

t = int(input())
arr = [True] * 1000000

for i in range(2,int(1000000**0.5)+1):
    if arr[i] == True:
        for j in range(i,1000000,j**2):
            arr[j] = False

for _ in range(t):
    n = int(input())
    mn = float('inf')
    a,b=0,0
    for i in range(2,n):
        if arr[i] and arr[n-i]:
            if abs(2 * i - n) < mn:
                mn = abs(2 * i - n)
                a = i
                b = n-i
    print(a,b)