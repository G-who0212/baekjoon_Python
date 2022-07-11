N, M, K = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
firstBig = a[N-1]
secondBig = a[N-2]
sum = 0

while True:
    for _ in range(K):
        if M == 0:
            break
        sum += firstBig
        M -= 1
    if M == 0: break
    else:
        sum += secondBig
        M -= 1

print(sum)