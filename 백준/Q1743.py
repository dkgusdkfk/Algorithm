import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [[False] * m for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    arr[r-1][c-1] = True

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
def dfs(x, y):
    cnt = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny]:
                arr[nx][ny] = False
                cnt += dfs(nx, ny)
    return cnt

result = 0
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            arr[i][j] = False
            result = max(result, dfs(i, j))
print(result)