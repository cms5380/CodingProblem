import sys

def solution(turn, l, r):
    global cards, dp
    if l == r:
        if turn == 0: return cards[l]
        else: return 0

    tmp = dp[turn][l][r]
    if tmp != -1:
        return tmp

    if turn:
        tmp = min(solution(turn ^ 1, l + 1, r), solution(turn ^ 1, l, r - 1))
    else:
        tmp = max(solution(turn ^ 1, l + 1, r) + cards[l], solution(turn ^ 1, l, r - 1) + cards[r])
    
    return tmp


T = int(sys.stdin.readline())
cards = []
dp =[]
for _ in range(T):
    N = int(sys.stdin.readline())
    cards = list(map(int, sys.stdin.readline().split(' ')))

    dp = [[[-1 for _ in range(N)] for _ in range(N)] for _ in range(2)]
    print(solution(0, 0, N - 1))

    print("done")