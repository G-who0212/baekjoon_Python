import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
parent = [0] * (n+1)
q = deque([1])
visited[1] = True

while(q):
    x = q.popleft()
    for y in graph[x]:
        if not visited[y]:
            parent[y] = x
            q.append(y)
            visited[y] = True
            
for i in range(2, n+1):
    print(parent[i])