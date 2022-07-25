import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def dfs(graph, v, visited):
    hack = 0
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            hack += (dfs(graph, i, visited) + 1)
    return hack

max = 0
li = []
for i in range(1, n + 1):
    visited = [False] * (n+1)
    tmp = dfs(graph, i, visited)
    if max < tmp:
        max = tmp
        li = [i]
    elif max == tmp:
        li.append(i)
    else:
        continue
    
for i in li:
    print(i, end=' ')