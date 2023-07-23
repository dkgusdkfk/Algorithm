from collections import deque
import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]
for _ in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[x][y] = 1

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
def bfs(x, y):
    q = deque()
    q.append((x, y))
    c = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    c += 1
                    q.append((nx, ny))
    return c

count = 0
answer = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = 1
            answer.append(bfs(i, j))
            count += 1
print(count)
print(*sorted(answer))
