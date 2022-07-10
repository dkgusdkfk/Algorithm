import sys
import heapq

INF = int(1e9)

n, m = map(int, sys.stdin.readline().split())

graph = [[] for i in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

q = []
heapq.heappush(q, (0, 1))
distance[1] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

d = 0
array = []
for i in range(2, n+1):
    if distance[i] > d:
        array = [i]
        d = distance[i]
    elif distance[i] == d:
        array.append(i)

print(min(array), d, len(array))