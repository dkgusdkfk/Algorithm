from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 9:
            shark = (i, j)
            size = 2
            graph[i][j] = 0

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

time = 0
eat = 0


def bfs(r, c):
    global size, shark, time, eat
    visited = [[False] * n for _ in range(n)]
    queue = deque()
    queue.append((r, c, 0))
    visited[r][c] = True
    temp = []
    while queue:
        x, y, t = queue.popleft()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if 0 <= mx < n and 0 <= my < n:
                if visited[mx][my]: continue
                if graph[mx][my] == 0:
                    visited[mx][my] = True
                    queue.append((mx, my, t + 1))
                    continue
                if graph[mx][my] < size:
                    visited[mx][my] = True
                    temp.append((mx, my, t + 1))
                if graph[mx][my] == size:
                    queue.append((mx, my, t + 1))
                    visited[mx][my] = True

    if len(temp) == 0: return False
    temp = sorted(temp, key=lambda x: (x[2], x[0], x[1]))
    x, y, t = temp[0]
    graph[x][y] = 0
    eat += 1
    if eat >= size:
        eat -= size
        size += 1
    shark = (x, y)
    time += t
    return True


while bfs(shark[0], shark[1]):
    pass

print(time)
