n, m = map(int, input().split())
a = [[0] * m for _ in range(n)] # n행 m열
for i in range(n):
    a[i] = list(map(int, input().split()))

b = [0] * n
d = []
for i in range(n):
    c = []
    for j in range(m):
        c.append(a[i][j])
    d.append(min(c))

ans = max(d)

print(ans)