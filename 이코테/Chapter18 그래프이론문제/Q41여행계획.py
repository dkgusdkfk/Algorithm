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

n, m = map(int, input().split())

parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for i in range(1, n+1):
    array = list(map(int, sys.stdin.readline().split()))[i:]
    k = i + 1
    for a in array:
        if a == 1:
            union_parent(parent, i, k)
        k += 1

plan = list(map(int, input().split()))

result = 'YES'
for i in range(len(plan)-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        result = 'NO'
        break

print(result)