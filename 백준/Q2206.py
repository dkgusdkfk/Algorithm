from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input())[:-1] for _ in range(n)]
visited = [[[0, 0]] * m for _ in range(n)]

queue = deque()
queue.append((0, 0, 0))
visited[0][0][0] = 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
while queue:
    print(queue)
    x, y, z = queue.popleft()
    if (x, y) == (n-1, m-1):
        print(visited[x][y][z])
        exit(0)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        print(nx, ny, graph[nx][ny], visited[nx][ny][z])
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == '0':
                if visited[nx][ny][z] == 0:
                    queue.append((nx, ny, z))
                    visited[nx][ny][z] = visited[x][y][z] + 1
            elif graph[nx][ny] == '1' and z == 0:
                queue.append((nx, ny, z+1))
                visited[nx][ny][z+1] = visited[x][y][z] + 1
print(-1)