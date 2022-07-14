import sys

def input():
    sys.stdin.readline().rstrip()

N = int(input())
arr = []
sum = 0
for i in range(N):
    arr.append(int(input()))
arr.sort(key=lambda x : -x) # 람다함수를 이용한 거꾸로 정렬
for i in range(len(arr)):
    tip = arr[i] - i
    if tip > 0:
        sum += tip
print(sum)
