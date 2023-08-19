from collections import deque

MAX_VALUE = 100000

n, k = map(int, input().split())
queue = deque()
visited = [-1 for _ in range(MAX_VALUE+1)]
count = [0 for _ in range(MAX_VALUE+1)]
queue.append(n)
visited[n] = n

while queue:
    x = queue.popleft()
    if x == k:
        print(count[k])
        break
    if x - 1 >= 0 and visited[x-1] == -1:
        queue.append(x-1)
        visited[x-1] = x
        count[x-1] = count[x] + 1
    if x + 1 <= MAX_VALUE and visited[x+1] == -1:
        queue.append(x+1)
        visited[x + 1] = x
        count[x+1] = count[x] + 1
    if x*2 <= MAX_VALUE and visited[x*2] == -1:
        queue.append(x*2)
        visited[x*2] = x
        count[x*2] = count[x] + 1

arr = []
while n != k:
    arr.append(k)
    k = visited[k]
arr.append(n)
print(*arr[::-1])