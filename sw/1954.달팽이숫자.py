import sys
sys.stdin = open("input.txt", "r")

T = int(input())

# 시계방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for t in range(1, T+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]

    d = 0
    x, y = 0, 0
    for num in range(1, n*n + 1):
        arr[x][y] = num
        if not(0 <= x+dx[d] < n and 0 <= y+dy[d] < n and arr[x+dx[d]][y+dy[d]] == 0):
            d = (d + 1) % 4
        x += dx[d]
        y += dy[d]

    print("#%d" % t)
    for i in range(n):
        print(*arr[i])