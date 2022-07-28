import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
table = defaultdict(int)

for i in range(1, n+1):
    table[i] = int(input())
ans = set()

def dfs(v, first, second):
    first.add(v)
    second.add(table[v])
    if table[v] in first:
        if first == second:
            ans.update(first)
            return
        else:
            return
    dfs(table[v], first, second)
    
for i in range(1, n+1):
    if i not in ans:
        dfs(i, set(), set())

result = list(ans)
result.sort()
print(len(result))
for x in result:
    print(x)