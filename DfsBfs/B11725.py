import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [0] * (n+1)

q = deque([1])
visited[1] = 0

while q:
    x = q.popleft() 
    for e in graph[x]:
        if not visited[e]:
            q.append(e)
            visited[e] = visited[x] + 1

for i in range(2, len(graph)):
    graph[i].sort(key = lambda x : visited[x])
    
for i in range(2, len(graph)):
    print(graph[i][0])