import math

n = int(input())

a = list(map(int, input().split()))
b, c = map(int, input().split())

answer = 0
for i in a:
    i -= b
    if i <= 0:
        answer += 1
    else:
        answer += math.ceil(i/c) + 1

print(answer)