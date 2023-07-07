from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = []
minValue = 100
maxValue = 1
for i in range(n):
    graph.append(list(map(int, input().split())))
    minValue = min(minValue, min(graph[i]))
    maxValue = max(maxValue, max(graph[i]))
minValue -= 1
maxValue -= 1

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def check(k):
    temp = [g[:] for g in graph]
    count = 0

    for i in range(n):
        for j in range(n):
            if temp[i][j] > k:
                q = deque()
                q.append((i, j))
                temp[i][j] = 0
                while q:
                    x, y = q.popleft()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if not(0 <= nx < n and 0 <= ny < n):  continue
                        if temp[nx][ny] > k:
                            q.append((nx, ny))
                            temp[nx][ny] = 0
                count += 1
    return count

def main():
    ans = 0
    for i in range(minValue, maxValue + 1):
        ans = max(ans, check(i))
    print(ans)

main()