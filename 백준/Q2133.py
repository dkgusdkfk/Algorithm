n = int(input())
if n % 2 != 0:
    print(0)
else:
    dp = [0] * (n+1)
    dp[0] = 1
    if n >= 2:
        dp[2] = 3
    if n > 2:
        temp = dp[0] + dp[2]
        for i in range(4, n+1, 2):
            dp[i] = dp[i-2] * 3 + temp * 2
            temp += dp[i]
    print(dp[n])