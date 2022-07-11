n = int(input())
nList = []

for _ in range(n):
    nList.append(int(input()))
    
nList.sort()

for i in range(n):
    print(nList[i])