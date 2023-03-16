import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.insert(0, 0)
knapsack = [[0] * (K + 1) for _ in range(N + 1)]

for n in range(1, N + 1):
    for k in range(1, K + 1):
        w = arr[n][0]
        v = arr[n][1]

        if w > k:
            knapsack[n][k] = knapsack[n - 1][k]
        else:
            knapsack[n][k] = max(knapsack[n - 1][k - w] + v, knapsack[n - 1][k])
print(knapsack[N][K])