n = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(1, n+1):
    graph[i] = int(input())
    
def dfs(graph, v, k):
    visited[v] = True
    global mark
    mark += 1
    dfs(graph, graph[v], k)
    if graph[v] == k:
        return v
    elif graph[v] == v:
        mark = -1
        return v
    elif visited[graph[v]]:
        mark = -2
        return v
        

ans = []
for i in range(1, n+1):
    mark = 0
    visited = [False] * (n+1)
    if not visited[i]:
        x = dfs(graph, i, i)
        if mark == -1:
            ans.append(x)
        elif mark == -2:
            continue
        else:
            for j in range(mark+1):
                ans.append(x + j)

ans.sort()

print(len(ans))
for x in ans:
    print(x)
    
# checked = [False] * (n + 1)


# ans = []
# for i in range(1, n + 1):
#     if not checked[i]:
#         if li[li[i]] == i:
#             if i != li[i]:
#                 checked[i] = True
#                 ans.append(i)
#                 checked[li[i]] = True
#                 ans.append(li[i])
#             else:
#                 checked[i] = True
#                 ans.append(i)

# ans.sort()
# print(len(ans))

# for x in ans:
#     print(x)