import sys
r = sys.stdin.readline

num_8 = r().strip()
if num_8 == '0':
    print(num_8)
else:
    for i, n in enumerate(num_8):
        idx = 2
        n = int(n)
        tmp = ['0'] * 3
        while n > 0:
            tmp[idx] = str(n % 2)
            n = n // 2
            idx -= 1
        
        if i == 0:
            for j in range(idx+1, 3):
                print(tmp[j], end='')
        else:
            print(''.join(tmp), end='')