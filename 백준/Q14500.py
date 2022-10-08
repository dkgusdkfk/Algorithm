n, m = map(int, input().split())

paper = []
for i in range(n):
    paper.append(list(map(int, input().split())))

visited = [[0 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

maxTotal = 0


def dfs(x, y, total, count):
    global maxTotal
    if count == 4:
        maxTotal = max(maxTotal, total)
        return

    if (0 <= x < n) and (0 <= y < m):
        if visited[x][y] == 0:
            for k in range(4):
                visited[x][y] = 1
                dfs(x + dx[k], y + dy[k], total + paper[x][y], count + 1)
                visited[x][y] = 0


def plus(x, y, total):
    global maxTotal
    for i in range(4):
        total = paper[x][y]
        for j in range(3):
            if 0 <= x + dx[(i + j) % 4] < n and 0 <= y + dy[(i + j) % 4] < m:
                total += paper[x + dx[(i + j) % 4]][y + dy[(i + j) % 4]]
        maxTotal = max(maxTotal, total)


for i in range(n):
    for j in range(m):
        dfs(i, j, 0, 0)
        plus(i, j, 0)

print(maxTotal)