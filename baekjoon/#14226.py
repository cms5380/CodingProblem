from collections import deque

S = int(input())

q = deque()
q.append((1,0,0))
visit = set()
visit.add((1,0))
while q:
    cur, clip, dep = q.popleft()

    if cur == S:
        print(dep)
        break

    
    if (cur,cur) not in visit:
        q.append((cur, cur, dep + 1))
        visit.add((cur,cur))
    if cur > 0 and (cur - 1, clip) not in visit:
        q.append((cur-1, clip, dep + 1))
        visit.add((cur - 1, clip))

    if clip != 0 and (cur + cur, cur):
        q.append((cur + clip, clip, dep + 1))
        visit.add((cur + cur, cur))

    
