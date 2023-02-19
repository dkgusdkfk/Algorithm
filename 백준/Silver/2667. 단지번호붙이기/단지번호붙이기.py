from collections import deque

n = int(input())
graph = [list(map(int, list(input()))) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

queue = deque()


def bfs(k):
    global result
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if not (0 <= mx < n and 0 <= my < n):
                continue
            if graph[mx][my] == 1:
                graph[mx][my] = k
                result[k - 2] += 1
                queue.append((mx, my))


result = []
value = 1
for r in range(n):
    for c in range(n):
        if graph[r][c] == 1:
            value += 1
            result.append(1)
            graph[r][c] = value
            queue.append((r, c))
            bfs(value)

print(value - 1)
for r in sorted(result):
    print(r)