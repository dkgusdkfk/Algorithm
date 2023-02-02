n, m = map(int, input().split())
r, c, d = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph = [list(map(int, input().split())) for _ in range(n)]

result = 0

while True:
    result += 1 if graph[r][c] == 0 else 0
    graph[r][c] = 2
    flag = 0
    for i in range(1, 5):
        mx = r + dx[(d - i) % 4]
        my = c + dy[(d - i) % 4]
        if graph[mx][my] == 0:
            r = mx
            c = my
            d = (d-i) % 4
            flag = 1
            break
    if flag == 1 : continue
    mx = r + dx[(d+2) % 4]
    my = c + dy[(d+2) % 4]
    if graph[mx][my] != 1:
        r = mx
        c = my
    else:
         break

print(result)
