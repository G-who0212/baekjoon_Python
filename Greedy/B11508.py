import sys
input = sys.stdin.readline

n = int(input())
p = []
for _ in range(n):
    p.append(int(input()))
    
p.sort(reverse=True)

d = n // 3
k = n % 3

ans = 0

ans = sum(p)

for i in range(d):
    ans -= p[3*i + 2]
    
print(ans)