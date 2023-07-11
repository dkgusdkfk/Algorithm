from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isValid(nx, ny):
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = 0
                    count += 1
    return count


def isValid(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False

def main():
    total = 0
    maxValue = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                total += 1
                maxValue = max(maxValue, bfs(i, j))
    print(total)
    print(maxValue)

main()