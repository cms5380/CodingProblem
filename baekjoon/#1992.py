import sys
from collections import *
input = sys.stdin.readline

n = int(input())
pic = [list(input().strip()) for _ in range(n)]

def func(x,y,size):
    if size == 1:
        print(pic[x][y],end='')
        return
    
    zero = True
    one = True

    for i in range(x,x+size):
        for j in range(y, y+size):
            if pic[i][j]=='1':
                zero=False
            else:
                one=False
    
    if zero:
        print(0,end='')
    elif one:
        print(1, end='')
    else:
        print('(', end='')
        func(x,y,size//2)
        func(x,y+size//2,size//2)
        func(x+size//2,y,size//2)
        func(x+size//2,y+size//2,size//2)
        print(')',end='')

    return

func(0,0,n)
