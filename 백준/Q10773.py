from collections import deque
k = int(input())

q = deque()
for _ in range(k):
    n = int(input())
    if n == 0:
        q.pop()
    else:
        q.append(n)

print(sum(q))