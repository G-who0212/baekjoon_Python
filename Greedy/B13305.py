n = int(input())
r = list(map(int, input().split()))
p = list(map(int, input().split()))
ans = 0

x = 1000000001

for i in range(n-1):
    if p[i] < x:
        ans += p[i] * r[i]
        x = p[i]
    else:
        ans += x * r[i]
print(ans)