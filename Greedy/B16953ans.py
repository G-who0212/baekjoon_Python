from collections import deque

a, b = map(int, input().split())
res = -1
q = deque([(a, 0)])

while q:
    i, cnt = q.popleft()
    if b == i:
        res = cnt
        break
    else:
        if(a*2 <= b):
            q.append((i*2, cnt + 1))
        if((i*10)+1 <= b):
            q.append(((i*10)+1, cnt + 1))
if(res == -1): print(res)
else: print(res + 1)