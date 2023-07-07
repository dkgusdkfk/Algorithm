from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def melt():
    global graph
    temp = [g[:] for g in graph]

    for r in range(1, n):
        for c in range(1, m):
            if graph[r][c] > 0:
                temp[r][c] = graph[r][c] - counting(r, c)
                if temp[r][c] < 0:
                    temp[r][c] = 0
    graph = temp

def counting(x, y):
    count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if graph[nx][ny] == 0:
            count += 1
    return count

def check():
    temp = [g[:] for g in graph]

    count = 0
    for r in range(1, n):
        for c in range(1, m):
            if temp[r][c] > 0:
                bfs(r, c, temp)
                count += 1
    return count
def bfs(a, b, temp):
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if temp[nx][ny] > 0:
                q.append((nx, ny))
                temp[nx][ny] = 0

def main():
    time = 0
    while True:
        time += 1
        melt()
        count = check()
        if count == 0:
            time = 0
            break
        elif count >= 2:
            break
    print(time)

main()