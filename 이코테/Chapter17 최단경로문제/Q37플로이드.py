import sys

INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0
"""아래랑 다른점?
for a in range(1, n+1):
    graph[a][a] = 0
"""

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
