from collections import deque

n, l, r = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

#array = [[0]*n]*n

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def process(x, y, index):
    united = []
    united.append((x,y))
    q = deque()
    q.append((x,y))
    union[x][y] = index
    summary = graph[x][y]
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx,ny))
    for i, j in united:
        graph[i][j] = summary // count
    return count

total_count = 0

while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1
    if index == n * n:
        break
    total_count += 1

print(total_count)

"""
def dfs(x, y, count, k):
    for i in range(4):
        if 0 <= x+dx[i] < n and 0 <= y+dy[i] < n and arr[x+dx[i]][y+dy[i]] != k:
            if l <= abs(graph[x][y] - graph[x+dx[i]][y+dy[i]]) <= r:
                arr[x][y] = k
                arr[x+dx[i]][y+dy[i]] = k
                count += 1
                count = dfs(x+dx[i], y+dy[i], count, k)
    return count

result = 0

while (True):
    arr = [a[:] for a in array]
    dic = {}
    k = 1
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                c = dfs(i, j, 1, k)
                if c > 1:
                    dic[k] = c
                    k += 1
    if k == 1:
        break
    for i in range(1, k):
        klist = []
        sum = 0
        for x in range(n):
            for y in range(n):
                if arr[x][y] == i:
                    klist.append([x,y])
                    sum += graph[x][y]
        for x, y in klist:
            graph[x][y] = sum//dic[i]
    result += 1

print(result)
"""