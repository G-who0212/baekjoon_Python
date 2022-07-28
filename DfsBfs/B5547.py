import sys
from collections import deque, defaultdict
input = sys.stdin.readline

w, h = map(int, input().split())
inpHome = defaultdict(list)
for i in range(h):
    inpHome[i].extend(list(map(int, input().split())))
home = [[0]*(w+2) for _ in range(h+2)]
for y in range(h):
    for x in range(w):
        home[y+1][x+1] = inpHome[y][x]
        
ans = 0
oddDx = [-1, 1, 0, 1, 0, 1]
oddDy = [0, 0, -1, -1, 1, 1]
evenDx = [-1, 1, -1, 0, -1, 0]
evenDy = [0, 0, -1, -1, 1, 1]

visited = [[False] * (w+2) for _ in range(h+2)]

def bfs(startX, startY):
    queue = deque([(startX, startY)])
    visited[startY][startX] = True
    global ans
    while queue:
        x, y = queue.popleft()
        if y % 2 == 1: # 홀수번째 줄일 때
            for i in range(6):
                nx = x + oddDx[i]
                ny = y + oddDy[i]
                if nx < 0 or ny < 0 or nx > w+1 or ny > h+1:
                    continue
                if home[ny][nx] == 1:
                    ans += 1
                elif home[ny][nx] == 0 and visited[ny][nx] == False:
                    queue.append((nx, ny))
                    visited[ny][nx] = True
        if y % 2 == 0: # 짝수번째 줄일 때
            for i in range(6):
                nx = x + evenDx[i]
                ny = y + evenDy[i]
                if nx < 0 or ny < 0 or nx > w+1 or ny > h+1:
                    continue
                if home[ny][nx] == 1:
                    ans += 1
                elif home[ny][nx] == 0 and visited[ny][nx] == False:
                    queue.append((nx, ny))
                    visited[ny][nx] = True
            
    
bfs(0, 0)
print(ans)