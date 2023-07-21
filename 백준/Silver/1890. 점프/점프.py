import sys
input = sys.stdin.readline

def isValid(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            continue
        # 오른쪽 점프
        if j + graph[i][j] < n:
            dp[i][j+graph[i][j]] += dp[i][j]
        # 아래쪽 점프
        if i + graph[i][j] < n:
            dp[i+graph[i][j]][j] += dp[i][j]
print(dp[-1][-1])