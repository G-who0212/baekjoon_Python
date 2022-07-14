n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a.sort()
b = []
for i in range(len(a)):
    b.append(a[i] * (len(a) - i))
ans = max(b)
print(ans)