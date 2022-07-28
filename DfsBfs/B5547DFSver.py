import sys
from collections import defaultdict
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
visited = [[False] * (w+2) for _ in range(h+2)]

def dfs(x, y):
    global ans
    if x<0 or y<0 or x>w+1 or y>h+1:
        return
    if home[y][x] == 1:
        ans += 1
    elif home[y][x] == 0 and visited[y][x] == False:
        visited[y][x] = True
        if y % 2 == 1:
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x+1, y-1)
            dfs(x, y+1)
            dfs(x+1, y+1)
        else:
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x-1, y-1)
            dfs(x, y-1)
            dfs(x-1, y+1)
            dfs(x, y+1)
            
dfs(0, 0)
print(ans)