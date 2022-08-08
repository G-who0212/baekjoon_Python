import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0]*(m+1) for _ in range(n+1)]
one = []
for i in range(1, n+1):
    inp = input()
    for j in range(1, m+1):
        if inp[j-1] == '1':
            one.append((j, i))
        graph[i][j] = int(inp[j-1])


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(X, Y):
    visited = [[0] * (m+1) for _ in range(n+1)]
    visited[1][1] = 1
    graph[Y][X] = 0
    q = deque([(1, 1)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 1 and ny >= 1 and nx <= m and ny <= n and visited[ny][nx] == 0 and graph[ny][nx] == 0:
                if nx == m and ny == n:
                    graph[Y][X] = 1
                    return visited[y][x] + 1
                else:
                    q.append((nx, ny))
                    visited[ny][nx] = visited[y][x] + 1
    graph[Y][X] = 1

ans = []
for s in one:
    x, y = s
    b = bfs(x, y)
    if b != None:
        ans.append(b)
    
noCrush = bfs(0, 0)
if noCrush != None:
    ans.append(noCrush)

if not ans:
    print(-1)
else:
    print(min(ans))