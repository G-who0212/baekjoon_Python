n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())
    
a.sort(reverse=True)

sum = 0
for i in range(len(a)):
    if(a[i] - i < 0):
        break
    else:
        sum  += a[i] - i
    
print(sum)
