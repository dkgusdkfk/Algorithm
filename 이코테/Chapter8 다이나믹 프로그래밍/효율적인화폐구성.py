# N, M 입력
N, M = map(int, input().split())

# 화폐 가치 입력
array = []
for i in range(N):
    array.append(int(input()))

# DP 테이블 초기화
d = [0] * 100001


for i in array:
    d[i] = 1

for i in range(0, min(array)):
    d[i] = -1

for i in range(min(array)+1, M+1):
    if i-max(array) > 0 and i not in array:
        d[i] = min([d[i-j]+1 for j in array if d[i-j] != -1])
    else:
        d[i] = -1

print(d[M])