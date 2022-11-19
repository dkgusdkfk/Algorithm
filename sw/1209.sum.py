import sys
sys.stdin = open("input.txt", "r")

for _ in range(1, 11):
    result = 0

    graph = []

    n = int(input())

    for _ in range(100):
        row = list(map(int, input().split()))
        result = max(result, sum(row))
        graph.append(row)

    r = 0
    l = 0
    for i in range(100):
        r += graph[i][i]
        l += graph[i][-1-i]

        v = 0
        for j in range(100):
            v += graph[j][i]
        result = max(result, v)
    result = max(result, r, l)

    print("#%d %d" % (n, result))