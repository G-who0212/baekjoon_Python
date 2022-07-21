import sys
input = sys.stdin.readline

n = int(input())
num = []

suma = 0
for i in range(n):
    x, a = map(int, input().split())
    suma += a
    num.append([x, a])

num.sort(key=lambda x : x[0])

accsum = 0

if suma % 2 == 1:
    suma += 1

for i in range(n):
    accsum += num[i][1]
    if accsum >= suma // 2:
        print(num[i][0])
        break