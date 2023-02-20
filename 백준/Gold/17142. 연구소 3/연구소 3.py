from collections import deque
from itertools import combinations

# 연구소의 크기 n, 바이러스의 개수 m
n, m = map(int, input().split())

graph = []
virus = []
for i in range(n):  # 0:빈칸, 1:벽, 2:바이러스
    g = list(map(int, input().split()))
    for j, k in enumerate(g):
        if k == 2:
            virus.append([i, j])
    graph.append(g)

array = list(combinations(virus, m))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

queue = deque()


def bfs(g):
    time = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if 0 <= mx < n and 0 <= my < n and visited[mx][my] == 0 and g[mx][my] != 1:
                if g[mx][my] == 0:
                    time = max(time, g[x][y] + 1)
                g[mx][my] = g[x][y] + 1
                visited[mx][my] = 1
                queue.append((mx, my))
    return time


result = 1e9
for arr in array:
    g = [gp[:] for gp in graph]
    visited = [[0] * n for _ in range(n)]

    for a in arr:
        visited[a[0]][a[1]] = 1
        g[a[0]][a[1]] = 0
        queue.append((a[0], a[1]))
    r = bfs(g)
    for a in arr:
        g[a[0]][a[1]] = 1

    if not (0 in list(map(min, g))):
        result = min(result, r)

if result == 1e9:
    print(-1)
else:
    print(result)