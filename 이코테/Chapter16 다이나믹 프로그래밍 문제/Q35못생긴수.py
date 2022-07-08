n = int(input())

dp = [0] * n

dp[0] = 1

a=0
b=0
c=0

for i in range(1, n):
    array = []
    if dp[a]*2 not in dp:
        array.append(dp[a]*2)
    else:
        a+=1
    if dp[b]*3 not in dp:
        array.append(dp[b]*3)
    else:
        b+=1
    if dp[c]*5 not in dp:
        array.append(dp[c]*5)
    else:
        c+=1

    if min(array) == dp[a]*2:
        dp[i] = dp[a]*2
        a += 1
    elif min(array) == dp[b]*3:
        dp[i] = dp[b]*3
        b += 1
    else:
        dp[i] = dp[c]*5
        c+=1

print(dp[-1])