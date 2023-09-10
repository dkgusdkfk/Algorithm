from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

parents = [0 for _ in range(n+1)]
queue = deque([1])
parents[1] = 1
while queue:
    now = queue.popleft()
    for next in tree[now]:
        if parents[next] == 0:
            parents[next] = now
            queue.append(next)

for k in parents[2:]:
    print(k)