import sys
from collections import deque

m, n = map(int, input().split())

# 1: 익은, 0: 안익은, -1: 빈칸
tomato = []
queue = deque([])
for i in range(n):
    tomato.append(list(map(int, input().split())))
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append([i, j])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while queue:
    r, c = queue.popleft()
    for i in range(4):
        mx = r + dx[i]
        my = c + dy[i]
        if 0 <= mx < n and 0 <= my < m:
            if tomato[mx][my] == 0:
                tomato[mx][my] = tomato[r][c] + 1
                queue.append([mx, my])

day = 0
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            exit(0)
        else:
            day = max(day, tomato[i][j])
print(day-1)