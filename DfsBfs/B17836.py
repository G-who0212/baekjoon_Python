import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n, m, t = map(int, input().split())

graph = defaultdict(list)
for i in range(1, n+1):
    graph[i].append(0)
    graph[i].extend(list(map(int, input().split())))
        
# graph = [[0]*(m+1) for _ in range(n+1)]
# for i in range(1, n+1):
#     graph[i].append(0)
#     graph[i].extend(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

greentmp = -1
greencheck = 0

def greenans():    
    record = [[-1]*(m+1) for _ in range(n+1)]
    record[1][1] = 0
    q = deque([(1, 1)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 1 and ny >= 1 and nx <= m and ny <= n and record[ny][nx] == -1:
                if graph[ny][nx] == 0:
                    q.append((nx, ny))
                    record[ny][nx] = record[y][x] + 1
                elif graph[ny][nx] == 2:
                    global greencheck
                    greencheck = 1
                    return record[y][x] + 1 + (n-ny) + (m-nx)

def orangeans():
    record = [[-1]*(m+1) for _ in range(n+1)]
    record[1][1] = 0
    q = deque([(1, 1)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 1 and ny >= 1 and nx <= m and ny <= n and record[ny][nx] == -1:
                if graph[ny][nx] != 1:
                    q.append((nx, ny))
                    record[ny][nx] = record[y][x] + 1
    return record[n][m]

gA = greenans()
oA = orangeans()

if greencheck == 0 and oA == -1:
    print("Fail")
    sys.exit()
elif greencheck != 0 and oA == -1:
    ans = gA
elif greencheck == 0 and oA != -1:
    ans = oA
else: ans = min(gA, oA)


if ans > t: print("Fail")
else: print(ans)