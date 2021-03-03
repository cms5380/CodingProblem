import sys
from collections import deque
def solution(S, bomb):
    s = deque()
    leng = len(bomb)
    for c in S:
        s.append(c)

        if c == bomb[-1] and ''.join(s[-leng:]) == bomb:
            del s[-leng:]
        
    ret = ''.join(s)

    return ret if len(ret) != 0 else "FRULA"

a = str(sys.stdin.readline().strip())
b = str(sys.stdin.readline().strip())
print(solution(a,b))