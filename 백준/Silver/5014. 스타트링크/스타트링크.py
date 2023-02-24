from collections import deque

F, S, G, U, D = map(int, input().split())

visited = [-1] * (F + 1)

queue = deque()


def bfs(k):
    queue.append(k)
    visited[k] = 0
    while queue:
        n = queue.popleft()
        if n == G:
            return
        if 1 <= n + U <= F:
            if visited[n + U] == -1:
                visited[n + U] = visited[n] + 1
                queue.append(n + U)
        if 1 <= n - D <= F:
            if visited[n - D] == -1:
                visited[n - D] = visited[n] + 1
                queue.append(n - D)


bfs(S)
if visited[G] == -1:
    print("use the stairs")
else:
    print(visited[G])