from collections import deque

n = int(input())
graph = [list(map(int, list(input()))) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

queue = deque()


def bfs():
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if not (0 <= mx < n and 0 <= my < n):
                continue
            if graph[mx][my] == 1:
                graph[mx][my] = 0
                queue.append((mx, my))
                cnt += 1
    return cnt


result = []
for r in range(n):
    for c in range(n):
        if graph[r][c] == 1:
            graph[r][c] = 0
            queue.append((r, c))
            result.append(bfs())

print(len(result))
for r in sorted(result):
    print(r)