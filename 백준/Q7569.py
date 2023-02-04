import sys
from collections import deque

m, n, h = map(int, input().split())

# 1: 익은, 0: 안익은, -1: 빈칸
tomato = []
queue = deque([])
for i in range(h):
    t = []
    for j in range(n):
        t.append(list(map(int, sys.stdin.readline().split())))
        for k in range(m):
            if t[j][k] == 1:
                queue.append([i, j, k])
    tomato.append(t)

dz = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]

while queue:
    i, r, c = queue.popleft()
    for j in range(6):
        mz = i + dz[j]
        mx = r + dx[j]
        my = c + dy[j]
        if 0 <= mz < h and 0 <= mx < n and 0 <= my < m:
            if tomato[mz][mx][my] == 0:
                tomato[mz][mx][my] = tomato[i][r][c] + 1
                queue.append([mz, mx, my])

day = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                print(-1)
                exit(0)
            else:
                day = max(day, tomato[i][j][k])
print(day-1)
