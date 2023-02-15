from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
for i in range(n):
    graph[i][i] = 1

course = list(map(int, input().split()))


def solution(k):
    queue = deque([])
    for i in range(n):
        if graph[k][i] == 1 and i != k:
            queue.append(i)
    while queue:
        idx = queue.popleft()
        for i in range(n):
            if i == k or i == idx:
                continue
            if graph[idx][i] == 1 and graph[k][i] == 0:
                graph[k][i] = 1
                queue.append(i)


for i in range(n):
    solution(i)

result = "YES"
for i in range(m - 1):
    if graph[course[i] - 1][course[i + 1] - 1] == 0:
        result = "NO"
        break
print(result)