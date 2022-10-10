import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    n = int(input())

    arr = list(map(int, input().split()))

    data = [0] * 1001

    for a in arr:
        data[a] += 1

    mc = max(data)

    answer = max([i for i, v in enumerate(data) if v == mc])

    print("#%d %d" % (n, answer))
