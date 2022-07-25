from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(start):
    count = 0
    visited = [False] * (n+1)
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        count += 1
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
    return count

max = []
tmpMax = 0

for i in range(1, n+1):
    tmpBFS = bfs(i)
    if tmpBFS > tmpMax:
        tmpMax = tmpBFS
        max = [i]
    elif tmpBFS == tmpMax:
        max.append(i)
    else:
        continue

for x in max:
    print(x, end=' ')