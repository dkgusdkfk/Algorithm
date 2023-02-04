from collections import deque

n, m = map(int, input().split())

# 1: 이동 가능 0: 불가능
graph = [list(map(int, list(input()))) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

queue = deque([])
queue.append([0, 0])
while queue:
    x, y = queue.popleft()
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if 0 <= mx < n and 0 <= my < m:
            if graph[mx][my] == 1:
                graph[mx][my] = graph[x][y] + 1
                queue.append([mx, my])

print(graph[n-1][m-1])