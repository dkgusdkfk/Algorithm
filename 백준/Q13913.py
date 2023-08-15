from collections import deque

MAX_VALUE = 100000

n, k = map(int, input().split())
queue = deque()
visited = [0 for _ in range(MAX_VALUE+1)]
count = [0 for _ in range(MAX_VALUE+1)]
queue.append(n)
visited[n] = n

while queue:
    x = queue.popleft()
    if x == k:
        print(count[k])
        break
    if x - 1 >= 0 and visited[x-1] == 0:
        queue.append(x-1)
        visited[x-1] = x
        count[x-1] = count[x] + 1
    if x + 1 <= MAX_VALUE and visited[x+1] == 0:
        queue.append(x+1)
        visited[x + 1] = x
        count[x+1] = count[x] + 1
    if x*2 <= MAX_VALUE and visited[x*2] == 0:
        queue.append(x*2)
        visited[x*2] = x
        count[x*2] = count[x] + 1

arr = []
while n != k:
    arr.insert(0, k)
    k = visited[k]
arr.insert(0, n)
print(*arr)