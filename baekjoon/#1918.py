from collections import deque
expression = input()
operations = ['+', '-', '*', '/']
alp = 'QWERTYUIOPASDFGHJKLZXCVBNM'
s = deque()
answer = ''
for i, c in enumerate(expression):
    if c in alp: answer += c
    elif c ==')':
        while True:
            top = s.pop()
            if top == '(': break

            answer += top
    elif c in operations or c == '(':
        if c in '+-':
            while s and s[-1] in '*/':
                top = s.pop()
                    
                answer+=top
        s.append(c)
    
while s:
    answer+=s.pop()
print(answer)