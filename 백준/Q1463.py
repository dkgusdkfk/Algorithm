n = int(input())

INF = int(1e9)
dp = [INF] * (n+1)
dp[n] = 0

for i in range(n, 1, -1):
    if i % 3 == 0:
        if dp[i//3] > dp[i]+1:
            dp[i//3] = dp[i] + 1
    if i % 2 == 0:
        if dp[i // 2] > dp[i] + 1:
            dp[i // 2] = dp[i] + 1
    if dp[i-1] > dp[i] + 1:
        dp[i-1] = dp[i] + 1

print(dp[1])