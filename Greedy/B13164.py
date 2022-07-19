import sys
input = sys.stdin.readline

n, k = map(int, input().split())
li = list(map(int, input().split()))

sub =[]

for i in range(1, n):
    sub.append(li[i]-li[i-1])

sub.sort(reverse=True)
a = 0

for i in range(k - 1):
    a += sub[i]

ans = sum(sub) - a
print(ans)