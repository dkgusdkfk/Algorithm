from itertools import combinations

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i,j))
        if graph[i][j] == 2:
            chicken.append((i,j))

array = combinations(chicken, m)

result = 1e9
for arr in array:
    distance = 0
    for h in house:
        d = 1e9
        for a in arr:
            ah = abs(a[0]-h[0]) + abs(a[1]-h[1])
            if ah < d:
                d = ah
        distance += d
    if distance < result:
        result = distance

print(result)