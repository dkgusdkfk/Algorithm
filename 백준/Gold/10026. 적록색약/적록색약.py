from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
arr = [list(input().strip()) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

queue = deque()


def bfs(x, y, cr):
    color = arr[x][y]
    queue.append((x, y))
    while queue:
        r, c = queue.popleft()
        if arr[r][c] == color:
            arr[r][c] = cr
            for d in range(4):
                mx = r + dx[d]
                my = c + dy[d]
                if 0 <= mx < n and 0 <= my < n:
                    queue.append((mx, my))


result = [0, 0]
for i in range(n):
    for j in range(n):
        if arr[i][j] in ['R', 'B']:
            bfs(i, j, arr[i][j].lower())
            result[0] += 1
        elif arr[i][j] == 'G':
            bfs(i, j, 'r')
            result[0] += 1
for i in range(n):
    for j in range(n):
        if arr[i][j] in ['r', 'b']:
            bfs(i, j, 1)
            result[1] += 1
print(*result)