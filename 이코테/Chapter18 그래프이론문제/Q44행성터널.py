import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
parent = [0] * (n)

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

edges = []
result = 0

for i in range(n):
    parent[i] = i

for i in range(n):
    x, y, z = graph[i]
    for j in range(i+1,n):
        a, b, c = graph[j]
        cost = min(abs(x-a), abs(y-b), abs(z-c))
        edges.append((cost, i, j))

edges.sort()

for edge in edges:
    cost, x, y = edge
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += cost

print(result)