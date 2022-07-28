import sys
from collections import defaultdict ## 정리 필요
input = sys.stdin.readline

n = int(input())
g = defaultdict(list)
for i in range(1, n+1):
    v = int(input())
    g[v].append(i)
    
checked = [0 for _ in range(n+1)]
result = []

def dfs(u, visited):
    visited.add(u)
    checked[u] = 1 # 중복 탐색을 피함
    for v in g[u]:
        if v not in visited:
            dfs(v, visited.copy())
        else:
            result.extend(list(visited)) # 정리 필요
            return
        
for i in range(1, n+1):
    if not checked[i]:
        dfs(i, set([]))
        
result.sort()
print(len(result))
for x in result:
    print(x)