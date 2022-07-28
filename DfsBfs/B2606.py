import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input())
l = int(input())

graph = defaultdict(list)
visited = defaultdict(bool)
for _ in range(l):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    visited[x] = False
    visited[y] = False

ans = 0

def bfs(x):
    global ans
    visited[x] = True
    queue = deque([x])
    while queue:
        y = queue.popleft()
        for m in graph[y]:
            if not visited[m]:
                queue.append(m)
                visited[m] = True
                ans += 1

bfs(1)
print(ans)