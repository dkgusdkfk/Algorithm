from collections import deque
R, C = map(int, input().split())

graph = []
fire = deque()
jihoon = deque()
for r in range(R):
    g = list(input())
    for c in range(C):
        if g[c] == 'J':
            jihoon.append((r, c))
            g[c] = '.'
        elif g[c] == 'F':
            fire.append((r, c))
    graph.append(g)
visited = [[False for _ in range(C)] for _ in range(R)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def spread():
    fSize = len(fire)
    while fSize > 0:
        x, y = fire.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] == '.':
                    graph[nx][ny] = 'F'
                    fire.append((nx, ny))
        fSize -= 1

t = 0
while jihoon:
    t += 1
    spread()
    jSize = len(jihoon)
    while jSize > 0:
        x, y = jihoon.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if graph[nx][ny] == '.' and not visited[nx][ny]:
                    jihoon.append((nx, ny))
                    visited[nx][ny] = True
            else:
                print(t)
                exit(1)
        jSize -= 1

print("IMPOSSIBLE")
