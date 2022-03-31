import heapq

# N, M, C 입력
N, M, C = map(int, input().split())

graph = [[] for _ in range(N+1)]

INF = int(1e9)
distance = [INF] * (N+1)

for _ in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y,Z))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(C)

count = 0
time = []
for i in range(1, N+1):
    if distance[i] != INF and i != C:
        count += 1
        time.append(distance[i])

print(count, max(time))
