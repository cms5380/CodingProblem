N = int(input())

l,r = 1, 1000000000
ans = 0
find = False
while l <= r:
    m = (l + r) // 2
    tmp = 0
    
    idx = 5
    while idx <= m:
        tmp += m//idx
        idx *= 5

    if N <= tmp:
        if N == tmp:
            ans = m
            find = True
        r = m - 1
    else:
        l = m + 1

if find:
    print(ans)
else:
    print(-1)