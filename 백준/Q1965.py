n = int(input())
boxes = list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp[0] = boxes[0]
for i in range(1, n):
    for j in range(1, i+1):
        if boxes[i-j] < boxes[i]:
            if dp[i] > dp[i-j] + 1:
                break
            dp[i] = dp[i-j] + 1
print(dp[-1])