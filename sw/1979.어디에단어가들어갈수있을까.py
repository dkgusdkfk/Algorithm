import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def row_check(r, c):
    count = 0
    while(graph[r][c] != 0):
        count += 1
        c += 1
        if c >= n:
            break
    return count == k

def col_check(r, c):
    count = 0
    while(graph[r][c] != 0):
        count += 1
        r += 1
        if r >= n:
            break
    return count == k

for t in range(1, T+1):
    result = 0

    n, k = map(int, input().split())

    graph = []
    for r in range(n):
        graph.append(list(map(int, input().split())))

    for r in range(n):
        for c in range(n):
            if c == 0 or graph[r][c-1] == 0:
                result += row_check(r, c)
            if r == 0 or graph[r-1][c] == 0:
                result += col_check(r, c)

    print("#%d %d" % (t, result))