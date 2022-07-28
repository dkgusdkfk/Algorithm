import sys
from collections import deque

INF = int(1e9)

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark = (i,j)

def bfs(x, y, size):
    dist = INF
    d = []
    graph2 = [[1 for _ in range(n)] for _ in range(n)]
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            print(graph2)
            print(nx,ny)
            if graph[nx][ny] > size:
                continue
            if graph2[nx][ny] == 1:
                graph2[nx][ny] = graph2[x][y] + 1
                queue.append((nx,ny))
                if graph[nx][ny] < size:
                    if graph2[nx][ny] == dist:
                        d.append((nx,ny))
                    elif graph2[nx][ny] < dist:
                        d = [(nx,ny)]
                        dist = graph2[nx][ny]
    return [d, dist]

size = 2
count = 0
time = 0
while True:
    array = bfs(shark[0], shark[1], size)
    if array[0] == []:
        break
    else:
        array[0].sort()
        time += array[1]
        count += 1
        shark = array[0][0]
    if count == size:
        size += 1
        count = 0

print(time)