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

n, m = map(int, sys.stdin.readline().split())
parent = [0] * (n)

edges = []
result = 0

for i in range(n):
    parent[i] = i

for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    edges.append((z, x, y))

edges.sort()

for edge in edges:
    z, x, y = edge
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
    else:
        result += z

print(result)