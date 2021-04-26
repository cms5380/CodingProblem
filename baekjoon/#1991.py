import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N)]

def preorder(res, cur):
    if cur == -1:
        return res

    res += chr(cur + ord('A'))
    res = preorder(res, graph[cur][0])
    res = preorder(res, graph[cur][1])

    return res

def inorder(res, cur):
    if cur == -1:
        return res
    
    res = inorder(res, graph[cur][0])
    res += chr(cur + ord('A'))
    res = inorder(res, graph[cur][1])

    return res

def postorder(res, cur):
    if cur == -1:
        return res

    res = postorder(res, graph[cur][0])
    res = postorder(res, graph[cur][1])
    res += chr(cur + ord('A'))

    return res
for _ in range(N):
    a,b,c = map(str, input().split())
    if a != '.':
        a = ord(a) - ord('A')
    else:
        a = -1
    if b != '.':
        b = ord(b) - ord('A')
    else:
        b = -1
    if c != '.':
        c = ord(c) - ord('A')
    else:
        c = -1

    graph[a] = [b,c]

print(preorder('', 0))
print(inorder('', 0))
print(postorder('', 0))