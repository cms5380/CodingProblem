import sys
used = 0
answer = 0
sentences = []
def countSen():
    global used, sentences
    ret = 0
    for sentence in sentences:
        flag = True
        for c in sentence:
            if used & (1 << (ord(c) - 97)) == 0:
                flag = False
                break
        if flag:
            ret += 1
    return ret

def dfs(cnt, idx):
    global used, answer
    if cnt == k:
        tmp = countSen()
        answer = answer if tmp < answer else tmp
        return
    
    for i in range(idx, 26):
        if used & (1 << i): continue
        used |= 1 << i
        dfs(cnt + 1, i)
        used &= ~(1 << i)

n, k = map(int, sys.stdin.readline().split(' '))
sentences = [sys.stdin.readline().strip() for _ in range(n)]
if k < 5:
    print(0)
else:
    used |= (1 << (ord('a')-97))
    used |= (1 << (ord('n')-97))
    used |= (1 << (ord('c')-97))
    used |= (1 << (ord('i')-97))
    used |= (1 << (ord('t')-97))
    dfs(5,0)
    print(answer)