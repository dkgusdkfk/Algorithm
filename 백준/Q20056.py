import copy

n, m, k = map(int, input().split())

# 방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

graph = [[[] for _ in range(n)] for _ in range(n)]
# for i in range(n):
#     print(graph[i])

location = set()

for i in range(m):
    # 행,열,질량,속력,방향
    r, c, m, s, d = map(int, input().split())
    graph[r-1][c-1].append([m, s, d])
    location.add((r-1, c-1))

while(k > 0 and len(location) != 0):
    llist = list(location)
    location = set()
    new_graph = [[[] for _ in range(n)] for _ in range(n)]
    for x, y in llist:
        arr = graph[x][y]
        for m, s, d in arr:
            mx = (x + s * dx[d]) % n
            my = (y + s * dy[d]) % n
            new_graph[mx][my].append([m, s, d])
            location.add((mx, my))
    graph = copy.deepcopy(new_graph)

    for x, y in location:
        if len(graph[x][y]) >= 2:
            tm = 0
            ts = 0
            dlist = []  # 0:짝수, 1:홀수
            l = len(graph[x][y])
            for m, s, d in graph[x][y]:
                tm += m
                ts += s
                if d % 2 == 0:
                    dlist.append(0)
                else:
                    dlist.append(1)
            m = tm // 5
            if m == 0:
                graph[x][y] = []
                continue
            s = ts // l
            graph[x][y] = []
            if dlist.count(0) == l or dlist.count(1) == l:
                dir = [0, 2, 4, 6]
            else:
                dir = [1, 3, 5, 7]
            for d in dir:
                graph[x][y].append([m, s, d])

    k -= 1

answer = 0
for x, y in location:
    for m, s, d in graph[x][y]:
        answer += m

print(answer)