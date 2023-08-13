from collections import deque

MAX_VALUE = 100000

n, k = map(int, input().split())
queue = deque()
visited = [0 for _ in range(MAX_VALUE+1)]
queue.append(n)
visited[n] = 1

while queue:
    x = queue.popleft()
    if x*2 <= MAX_VALUE and visited[x*2] == 0:
        queue.appendleft(x*2)
        visited[x*2] = visited[x]
    if x == k or 2*x == k:
        print(visited[k] - 1)
        break
    if x - 1 >= 0 and visited[x-1] == 0:
        queue.append(x-1)
        visited[x-1] = visited[x] + 1
    if x + 1 <= MAX_VALUE and visited[x+1] == 0:
        queue.append(x+1)
        visited[x+1] = visited[x] + 1
