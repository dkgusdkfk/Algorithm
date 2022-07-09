import sys

INF = int(1e9)

n, m = map(int, sys.stdin.readline().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = -1
    graph[b][a] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][b] == -1:
                if graph[k][b] == 1:
                    graph[a][k] = -1
                    graph[k][a] = 1
                elif graph[a][k] == 1:
                    graph[b][k] = 1
                    graph[k][b] = -1
            elif graph[a][b] == 1:
                if graph[k][a] == 1:
                    graph[b][k] = -1
                    graph[k][b] = 1
                elif graph[k][b] == -1:
                    graph[a][k] = 1
                    graph[k][a] = -1

count = 0
for i in range(1, n+1):
    if INF not in graph[i][1:]:
        count += 1
print(count)
