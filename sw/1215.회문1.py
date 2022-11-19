import sys
sys.stdin = open("input.txt", "r")

def row(r, c):
    word = ''
    for i in range(n):
        if c+i >= 8:
            return ''
        word += graph[r][c+i]

    return word

def col(r, c):
    word = ''
    for i in range(n):
        if r + i >= 8:
            return ''
        word += graph[r + i][c]

    return word

for t in range(1, 11):
    result = 0

    n = int(input())

    graph = [list(input()) for _ in range(8)]

    for i in range(8):
        for j in range(8):
            s = row(i, j)
            result += (s == s[::-1] if s != '' else 0)
            s = col(i, j)
            result += (s == s[::-1] if s != '' else 0)

    print("#%d %d" % (t, result))