n = int(input())

INF = int(1e9)
dp = [INF] * (n+1)
dp[n] = 0
visited = [-1] * (n+1)

for i in range(n, 1, -1):
    if i % 3 == 0:
        if dp[i//3] > dp[i]+1:
            dp[i//3] = dp[i] + 1
            visited[i//3] = i
    if i % 2 == 0:
        if dp[i // 2] > dp[i] + 1:
            dp[i // 2] = dp[i] + 1
            visited[i // 2] = i
    if dp[i-1] > dp[i] + 1:
        dp[i-1] = dp[i] + 1
        visited[i-1] = i

arr = [1]
idx = 1
while idx != n:
    arr.append(visited[idx])
    idx = visited[idx]
print(dp[1])
print(*arr[::-1])