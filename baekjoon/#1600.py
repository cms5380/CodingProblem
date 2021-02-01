import sys
from collections import deque

move1 = [(0,1),(1,0),(-1,0),(0,-1)]
move2 = [(2,1),(2,-1),(1,2),(-1,2),(-2,1),(-2,-1),(1,-2),(-1,-2)]

K = int(sys.stdin.readline())
W, H = map(int, sys.stdin.readline().split(" "))
check = [[[False]*(K+1) for _ in range(W)] for _ in range(H)]

board = []
for _ in range(H):
    board.append(list(map(int,sys.stdin.readline().split(' '))))

q = deque()

q.append((0,0,0,0))
check[0][0][0] = True
flag = False
while q:
    x,y, dep, h_move = q.popleft()

    if x == H-1 and y == W-1:
        print(dep)
        flag = True
        break

    for dx,dy in move1:
        nx = dx + x
        ny = dy + y

        if 0 <= nx < H and 0 <= ny < W:
            if check[nx][ny][h_move] == False:
                if board[nx][ny] == 0:
                    check[nx][ny][h_move] = True
                    q.append((nx,ny,dep+1,h_move))

    if h_move < K:
        for dx,dy in move2:
            nx = dx + x
            ny = dy + y

            if 0 <= nx < H and 0 <= ny < W:
                if check[nx][ny][h_move + 1] == False:
                    if board[nx][ny] == 0:
                        q.append((nx,ny,dep+1, h_move+1))
                        check[nx][ny][h_move+1] = True


if not flag:
    print(-1)