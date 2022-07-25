import sys
input = sys.stdin.readline

n = int(input())
col = input()

b = 0
r = 0

if col[0] == 'B':
    b += 1
else:
    r += 1

for i in range(1, len(col)-1):
    if col[i] != col[i-1]:
        if col[i] == 'B':
            b += 1
        else:
            r += 1
print(min(b, r) + 1)