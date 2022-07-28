# N, M, K 입력
N, M, K = map(int, input().split())
# N개의 수 입력
nums = list(map(int, input().split()))

# 정렬
nums.sort()

sum = 0
count = 0 # 연속으로 더한 횟수
for i in range(M):
    if count < K: # 연속으로 더한 횟수가 K번을 초과하지 않았을 경우 가장 큰 수 더하고 횟수 추가
        sum += nums[-1]
        count += 1
    else: # 연속으로 더한 횟수가 K번을 초과한 경우 두번째로 큰 수 더하고 연속 횟수 0으로 리셋
        sum += nums[-2]
        count = 0

print(sum) # 최종 결과 출력

"""
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
    
print(result)
"""