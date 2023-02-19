from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

queue = deque()


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            mx = x + dx[i]
            my = y + dy[i]
            if 0 <= mx < n and 0 <= my < m:
                if graph[mx][my] == 0:
                    queue.append([mx, my])
                    graph[mx][my] = graph[x][y] + 1


for r in range(n):
    for c in range(m):
        if graph[r][c] == 1:
            queue.append([r, c])
bfs()
print(max(map(max, graph)) - 1)