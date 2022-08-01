import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
data = []
for i in range(1, n+1):
    data.append(i)

no = []

for i in range(m):
    a, b = map(int, input().split())
    no.append([a, b])
    
result = list(combinations(data, 3))

count = 0
for x in result:
    for n in no:
        if (n[0] in x) and (n[1] in x):
            count += 1
            break
        
print(len(result) - count)