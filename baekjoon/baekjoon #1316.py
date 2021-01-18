def sol(n):
    ans = 0
    for _ in range(n):
        alp_set = set()
        s = str(input())
        prev = s[0]
        flag = True
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                continue
            else:
                if s[i + 1] in alp_set:
                    flag = False
                    break
                
                prev = s[i + 1]
                alp_set.add(s[i])
        if flag:
            ans += 1
    return ans
N = int(input())
print(sol(N))