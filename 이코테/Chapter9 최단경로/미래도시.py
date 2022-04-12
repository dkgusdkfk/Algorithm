# N, M 입력
N, M = map(int, input().split())

INF = int(1e9)
graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    graph[i][i] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# X, K 입력
X, K = map(int, input().split())

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

result = graph[1][K] + graph[K][X]
if result >= INF:
    print(-1)
else:
    print(result)