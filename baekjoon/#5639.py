import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

preOrder = []

def solution(start, end):
    if start > end:
        return

    div = end + 1

    for i in range(start + 1, end + 1):
        # 루트 보다 큰 지점 --> 오른쪽 서브 트리
        if preOrder[start] < preOrder[i]:
            div = i
            break

    solution(start + 1, div - 1)
    solution(div, end)
    print(preOrder[start])

def postOrder(start, end):
    if start > end:
        return
    idx = start + 1

    while True:
        if idx < end and preOrder[idx] < preOrder[start]:
            idx += 1
        else: break
    
    postOrder(start + 1, idx)
    postOrder(idx+1, end)
    print(preOrder[start])

while True:
    try:
        preOrder.append(int(input()))
    except:
        break

solution(0, len(preOrder)-1)