n, l, r = map(int, input().split())

A = []
for i in range(n):
    A.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(x, y, k, g):
    if B[x][y] != 0:
        return

    if l <= abs(A[x][y] - k) <= r:
        B[x][y] = g
        for i in range(4):
            if (0 <= x+dx[i] < n) and (0 <= y+dy[i] < n):
                check(x+dx[i], y+dy[i], A[x][y], g)

day = 0
while(True):

    B = [[0 for _ in range(n)] for _ in range(n)]

    group_dict = {}
    group = 0

    for i in range(n):
        for j in range(n):
            if B[i][j] == 0:
                group += 1
                check(i, j, A[i][j]+l, group)
            if B[i][j] in group_dict:
                group_dict[B[i][j]].append((i, j))
            else:
                group_dict[B[i][j]] = [(i, j)]

    if group == n*n:
        break

    for k, v in group_dict.items():
        total = 0
        for x, y in v:
            total += A[x][y]
        result = total // len(v)
        for x, y in v:
            A[x][y] = result


    day += 1

print(day)