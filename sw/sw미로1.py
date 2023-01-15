from collections import deque
import sys
sys.stdin = open("input.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(10):
    result = 0

    t = int(input())

    graph = []
    for i in range(16):
        g = [int(a) for a in str(input())]
        if 2 in g:
            start = (i, g.index(2))
        graph.append(g)

    queue = deque()
    queue.append(start)
    while queue and result == 0:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < 16 or 0 <= ny < 16):
                continue
            if graph[nx][ny] == 1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny))
            if graph[nx][ny] == 3:
                result = 1
                break
    print("#%d %d" % (t, result))