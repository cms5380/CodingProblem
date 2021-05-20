import sys
r = sys.stdin.readline

def timeToStr(sec):
    ret = ''

    hour = sec // 3600
    if hour < 10:
        ret += '0'
    ret += str(hour)
    sec %= 3600

    minute = sec // 60
    if minute < 10:
        ret += '0'
    ret += str(minute)
    sec %= 60

    if sec < 10:
        ret += '0'
    
    ret += str(sec)

    return ret

N, K = map(int, r().split())

time = N * 60 * 60 + 59 * 60 + 59

ans = 0

for i in range(time):
    tmp = timeToStr(i)

    if str(K) in tmp:
        ans += 1

print(ans)