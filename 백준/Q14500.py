n, m = map(int, input().split());

paper = []
for i in range(n):
    paper.append(list(map(int, input().split())))

array = []
for a in range(n):
    arr = []
    for b in range(m):
        arr.append(0)
    array.append(arr)

A = array

max = 0
def solution(x, y, total, count, array):
    global max
    total += paper[x][y]
    array[x][y] = 1
    count += 1
    if count == 4:
        if max < total:
            max = total
        return
    if (x + 1) < n:
        if array[x + 1][y] == 0:
            solution(x + 1, y, total, count, array)
    if (x - 1) >= 0:
        if array[x - 1][y] == 0:
            solution(x - 1, y, total, count, array)
    if (y + 1) < m:
        if array[x][y + 1] == 0:
            solution(x, y + 1, total, count, array)
    if (y - 1) >= 0:
        if array[x][y - 1] == 0:
            solution(x, y - 1, total, count, array)


for i in range(n):
    array = A
    for j in range(m):
        solution(i, j, 0, 0, array)

print(max)