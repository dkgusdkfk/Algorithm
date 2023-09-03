from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = True

    while q:
        now = q.popleft()
        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                q.append(next)


for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        count += 1

print(count)