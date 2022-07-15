n = int(input())
a = list(map(int, input().split()))
if(n % 2 == 1):
    a.append(0)
    a.sort()
    b = []
    for i in range((n + 1)//2):
        b.append(a[i] + a[n - i])
    print(max(b))
else:
    a.sort()
    b = []
    for i in range(n//2):
        b.append(a[i] + a[n - 1 - i])
    print(max(b))