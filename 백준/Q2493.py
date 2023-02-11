import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

buildings = list(map(int, input().split()))

queue = deque()
queue.append(0)

result = [0]
for i in range(1, n):
    flag = 0
    while queue:
        b = queue.pop()
        if buildings[b] > buildings[i]:
            result.append(b+1)
            queue.append(b)
            queue.append(i)
            flag = 1
            break
    if flag == 0:
        result.append(0)
        queue.append(i)

print(*result)