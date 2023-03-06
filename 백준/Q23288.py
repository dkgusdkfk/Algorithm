n, m, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

dice = [1, 2, 3, 4, 5, 6]

def move(d):
    if d == 0:
        dice[3], dice[0], dice[2], dice[5] = dice[0], dice[2], dice[5], dice[3]
    elif d == 1:
        dice[1], dice[0], dice[4], dice[5] = dice[5], dice[1], dice[0], dice[4]
    elif d == 2:
        dice[3], dice[0], dice[2], dice[5] = dice[5], dice[3], dice[0], dice[2]
    else:
        dice[1], dice[0], dice[4], dice[5] = dice[0], dice[4], dice[5], dice[1]

def dfs(x, y, z):
    global score
    if visited[x][y] or graph[x][y] != z:
        return
    score += z
    visited[x][y] = True
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if 0 <= mx < n and 0 <= my < m:
            dfs(mx, my, z)

result = 0
dir = 0
r, c = 0, 0
for _ in range(k):
    if not(0 <= r + dx[dir] < n and 0 <= c + dy[dir] < m):
        dir = (dir + 2) % 4
    r += dx[dir]
    c += dy[dir]
    visited = [[False] * m for _ in range(n)]
    move(dir)
    score = 0
    dfs(r, c, graph[r][c])
    # print(dir)
    # print(score)
    result += score
    print(dir)
    print(dice[0], graph[r][c])
    if dice[0] > graph[r][c]:
        dir = (dir - 1) % 4
    elif dice[0] < graph[r][c]:
        dir = (dir + 1) % 4

print(result)
