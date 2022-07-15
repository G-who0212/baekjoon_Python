a, b = map(int, input().split())
ans = 0
while(1):
    if(a == b):
        break
    if(b < a):
        ans = -1
        break
    else:
        if(b % 2 == 0):
            b //= 2
            ans += 1
        elif(b % 10 == 1):
            b = b // 10
            ans += 1
        else:
            ans = -1
            break
        
if(ans == -1):
    print(-1)
else:
    print(ans + 1)