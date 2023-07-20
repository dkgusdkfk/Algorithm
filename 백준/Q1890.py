from collections import deque
import sys
input = sys.stdin.readline

def isValid(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

q = deque()
q.append((0, 0))
count = 0
while q:
    x, y = q.popleft()
    if x == n-1 and y == n-1:
        count += 1
        continue
    # 오른쪽 점프
    rx, ry = x, y + graph[x][y]
    if isValid(rx, ry):
        q.append((rx, ry))
    # 아래쪽 점프
    ux, uy = x + graph[x][y], y
    if isValid(ux, uy):
        q.append((ux, uy))
print(count)

