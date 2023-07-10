n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def dfs(x, y, c):
    print(x, y)
    if graph[x][y] != 1:    return c
    graph[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if isValid(nx, ny):
            c = dfs(nx, ny, c+1)
    return c

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
                print(dfs(i, j, 0))
                maxValue = max(maxValue, dfs(i, j, 0))
    print(total)
    print(maxValue)

main()