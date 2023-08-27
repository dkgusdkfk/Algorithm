from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

w, h = map(int, input().split())

while (w, h) != (0, 0):
    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))
    visited = [[False] * w for _ in range(h)]

    q = deque()
    count = 0
    for r in range(h):
        for c in range(w):
            if graph[r][c] == 1:
                count += 1
                q.append((r, c))
                visited[r][c] = True
                while q:
                    x, y = q.popleft()
                    for i in range(8):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < h and 0 <= ny < w:
                            if graph[nx][ny] == 1 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                graph[nx][ny] = 0
                                q.append((nx, ny))
    print(count)
    w, h = map(int, input().split())