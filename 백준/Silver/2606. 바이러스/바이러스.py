from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

arr = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(k):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

queue = deque()


def bfs(start):
    queue.append(start)
    visited[start] = 1
    while queue:
        s = queue.popleft()
        for i in arr[s]:
            if visited[i]:
                continue
            queue.append(i)
            visited[i] = 1
    return visited.count(1) - 1


print(bfs(1))