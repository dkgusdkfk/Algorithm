from collections import deque
import sys
input = sys.stdin.readline

dx = [0, -1, 0, 0, 1, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [-1, 0, 0, 0, 0, 1]

L, R, C = map(int, input().split())

while (L, R, C) != (0, 0, 0):
    graph = []
    queue = deque()
    for l in range(L):
        g = []
        for r in range(R):
            g.append(list(input()))
            for c in range(C):
                if g[r][c] == 'S':
                    queue.append((l, r, c))
        graph.append(g)
        input()

    result = 1
    flag = 0
    while queue:
        qSize = len(queue)
        while qSize > 0:
            qSize -= 1
            z, x, y = queue.popleft()
            for i in range(6):
                nz = z + dz[i]
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C:
                    if graph[nz][nx][ny] == '.':
                        queue.append((nz, nx, ny))
                        graph[nz][nx][ny] = '#'
                    elif graph[nz][nx][ny] == 'E':
                        print("Escaped in %d minute(s)." % (result))
                        flag = 1
                        break
            if flag == 1:
                break
        if flag == 1:
            break
        result += 1
    if flag == 0:
        print("Trapped!")
    L, R, C = map(int, input().split())