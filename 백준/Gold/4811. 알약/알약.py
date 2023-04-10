N = int(input())

while N != 0:
    dp = [[0] * (N+1) for _ in range(N+1)]

    for i in range(N+1):
        dp[0][i] = 1
    for i in range(1, N+1):
        for j in range(i, N+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    print(dp[N][N])
    N = int(input())