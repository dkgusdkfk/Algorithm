from collections import deque
import sys
input = sys.stdin.readline

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

t = int(input())

for _ in range(t):
    n = int(input())
    visited = [[False] * n for _ in range(n)]

    sx, sy = map(int, input().split())  # 나이트 시작 칸
    ex, ey = map(int, input().split())  # 나이트 도착 칸

    q = deque()
    q.append((sx, sy, 0))
    visited[sx][sy] = True

    while q:
        x, y, c = q.popleft()
        if (x, y) == (ex, ey):
            print(c)
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, c+1))

