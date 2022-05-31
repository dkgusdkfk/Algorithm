n, L, R = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

array = [[0]*n]*n

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, count, k):
    for i in range(4):
        if 0 <= x+dx[i] < n and 0 <= y+dy[i] < n and arr[x+dx[i]][y+dy[i]] != k:
            if L <= abs(graph[x][y] - graph[x+dx[i]][y+dy[i]]) <= R:
                arr[x][y] = k
                arr[x+dx[i]][y+dy[i]] = k
                count += 1
                dfs(x+dx[i], y+dy[i], count, k)
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
    for i in range(k):
        klist = []
        sum = 0
        for x in range(n):
            for y in range(n):
                if arr[x][y] == k:
                    klist.append([x,y])
                    sum += graph[x][y]
        for x, y in klist:
            graph[x][y] = sum/dic[k]
    result += 1

print(result)