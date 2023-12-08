import sys
input = sys.stdin.readline

n, k = map(int, input().split(" "))
tempList = list(map(int, input().split(" ")))

answer = sum(tempList[:k])
temp = answer
for i in range(k, n):
    temp += tempList[i] - tempList[i-k]
    answer = max(answer, temp)

print(answer)