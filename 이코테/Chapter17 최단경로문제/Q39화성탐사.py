import sys
import heapq

INF = int(1e9)

t = int(sys.stdin.readline())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(t):
    n = int(sys.stdin.readline())
    graph = []
    for i in range(n):
        graph.append(list(map(int, sys.stdin.readline().split())))
    distance = [[INF for _ in range(n)] for _ in range(n)]

    q = []
    heapq.heappush(q, (0, (0,0)))
    distance[0][0] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now[0]][now[1]] < dist:
            continue
        for i in graph[now[0]][now[1]]:
            cost = dist + i[1]
