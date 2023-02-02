n, m, x, y, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

order = list(map(int, input().split()))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dice = [0, 0, 0, 0, 0, 0]
# dice = [0,1,2,3,4,5]

result = []

def move(d, c):
    if d == 1:
        dice[3], dice[0], dice[2], dice[5] = dice[0], dice[2], dice[5], dice[3]
    elif d == 2:
        dice[3], dice[0], dice[2], dice[5] = dice[5], dice[3], dice[0], dice[2]
    elif d == 3:
        dice[1], dice[0], dice[4], dice[5] = dice[5], dice[1], dice[0], dice[4]
    else:
        dice[1], dice[0], dice[4], dice[5] = dice[0], dice[4], dice[5], dice[1]
    result.append(dice[5])
    if c == 0:
        return dice[0]
    else:
        dice[0] = c
        return 0


for o in order:
    mx = x + dx[o-1]
    my = y + dy[o-1]
    if 0 <= mx < n and 0 <= my < m:
        graph[mx][my] = move(o, graph[mx][my])
        x = mx
        y = my

for r in result:
    print(r)
