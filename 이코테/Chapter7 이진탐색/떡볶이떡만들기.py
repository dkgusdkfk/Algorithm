# N, M 입력
N, M = map(int, input().split())

# 떡의 개별 높이 입력
array = list(map(int, input().split()))

for H in range(max(array), 0, -1):
    total = 0
    for n in range(N):
        t = array[n] - H
        if t > 0:
            total += t
    if total == M:
        break

print(H)