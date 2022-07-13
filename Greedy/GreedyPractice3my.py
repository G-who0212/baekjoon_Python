n, k = map(int, input().split())
ans = 0

while(n != 1):
    if(n % k == 0):
        n = n // k
        ans = ans + 1
    else:
        n = n - 1
        ans = ans + 1
print(ans)