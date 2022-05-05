def solution(n, s, a, b, fares):
    answer = 0

    INF = int(1e9)

    graph = [[INF]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        graph[i][i] = 0

    for f in fares:
        f1, f2, f3 = f
        graph[f1][f2] = f3
        graph[f2][f1] = f3

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    answer_min = int(1e9)
    for i in range(1, n+1):
        if graph[s][i] + graph[i][a] + graph[i][b] < answer_min:
            answer_min = graph[s][i] + graph[i][a] + graph[i][b]

    answer = answer_min

    return answer


fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(6, 4, 6, 2, fares))