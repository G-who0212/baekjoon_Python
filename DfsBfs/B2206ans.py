import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

visited = [[[0]*2 for _ in range(m)] for _ in range(n)] # 3차원 배열
visited[0][0][0] = 1
visited[0][0][1] = 1

q = deque([(0, 0, 0)])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while q:
        x, y, c = q.popleft()
        if x == m-1 and y == n-1:
            return visited[y][x][c]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < m and ny < n:
                if graph[ny][nx] == 1 and c == 0:
                    visited[ny][nx][1] = visited[y][x][0] + 1
                    q.append((nx, ny, 1))
                elif graph[ny][nx] == 0 and visited[ny][nx][c] == 0:
                    visited[ny][nx][c] = visited[y][x][c] + 1
                    q.append((nx, ny, c))
    return -1

print(bfs())