n, m = map(int, input().split())

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

array = []

for i in range(m):
    a, b, c = map(int, input().split())
    array.append([c, a, b])

array.sort()


def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


result = 0
max_cost = 0
for ar in array:
    cost, a, b = ar
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        if max_cost < cost:
            max_cost = cost

result -= max_cost

print(result)
