from collections import deque

n, m, v = map(int, input().split())

graph = []
for i in range(m):
    graph.append(list(map(int, input().split())))


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    node = []
    for i in range(m):
        for j in range(2):
            if graph[i][j] == v:
                node.append(graph[i][(2 + (j - 1)) % 2])
    node.sort()
    for i in node:
        if not visited[i]:
            dfs(graph, i, visited)


visited = [False] * (n + 1)

dfs(graph, v, visited)

print()

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        node = []
        for i in range(m):
            for j in range(2):
                if graph[i][j] == v:
                    node.append(graph[i][(2 + (j - 1)) % 2])
        node.sort()
        for i in node:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


visited = [False] * (n + 1)

bfs(graph, v, visited)
