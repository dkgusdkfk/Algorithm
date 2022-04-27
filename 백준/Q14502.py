n, m = map(int, input().split())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))
board = []
for i in range(n):
    b = []
    for j in range(m):
        b.append(array[i][j])
    board.append(b)

zero = []
virus = []
for x in range(n):
    for y in range(m):
        if array[x][y] == 0:
            zero.append([x,y])
        elif array[x][y] == 2:
            virus.append([x,y])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def spread(x, y, array):
    if array[x][y] == 0:
        array[x][y] = 2
        for s in range(4):
            if 0 <= x + dx[s] < n and 0 <= y + dy[s] < m:
                spread(x+dx[s], y+dy[s], array)

def is_safe(array):
    count = 0
    for x in range(n):
        for y in range(m):
            if array[x][y] == 0:
                count += 1
    return count

max = 0
for i in range(len(zero)-2):
    for j in range(i+1, len(zero)-1):
        for k in range(j+1, len(zero)):
            array[zero[i][0]][zero[i][1]] = 1
            array[zero[j][0]][zero[j][1]] = 1
            array[zero[k][0]][zero[k][1]] = 1
            for v in range(len(virus)):
                array[virus[v][0]][virus[v][1]] = 0
                spread(virus[v][0], virus[v][1], array)
            safe = is_safe(array)
            if safe > max:
                max = safe
            array = []
            for i in range(n):
                a = []
                for j in range(m):
                    a.append(board[i][j])
                array.append(a)
            print(array)
            # array[zero[i][0]][zero[i][1]] = 0
            # array[zero[j][0]][zero[j][1]] = 0
            # array[zero[k][0]][zero[k][1]] = 0

print(max)