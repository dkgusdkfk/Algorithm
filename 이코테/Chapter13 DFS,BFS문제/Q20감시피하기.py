from itertools import combinations

# 지도의 세로크기 n, 가로크기 m
n, m = map(int, input().split())

graph = []
for i in range(n):  # 0:빈칸, 1:벽, 2:바이러스
    graph.append(list(map(int, input().split())))

blank = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            blank.append((i,j))

array = list(combinations(blank, 3))

def dfs(x, y, g):
    if 0 <= x < n and 0 <= y < m:
        if g[x][y] == 0:
            g[x][y] = 2
            dfs(x-1, y, g)
            dfs(x, y-1, g)
            dfs(x+1, y, g)
            dfs(x, y+1, g)

maxCount = 0
for arr in array:
    g = [gp[:] for gp in graph]

    for a in arr:
        g[a[0]][a[1]] = 1

    for i in range(n):
        for j in range(m):
            if g[i][j] == 2:
                g[i][j] = 0
                dfs(i, j, g)

    count = 0
    for i in range(n):
        count += g[i].count(0)

    if count > maxCount:
        maxCount = count

print(maxCount)