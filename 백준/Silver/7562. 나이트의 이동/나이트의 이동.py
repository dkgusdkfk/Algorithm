from collections import deque
import sys
input = sys.stdin.readline

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

t = int(input())

for _ in range(t):
    n = int(input())
    visited = [[0] * n for _ in range(n)]

    sx, sy = map(int, input().split())  # 나이트 시작 칸
    ex, ey = map(int, input().split())  # 나이트 도착 칸

    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = 1

    while q:
        x, y = q.popleft()
        if (x, y) == (ex, ey):
            print(visited[x][y]-1)
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))