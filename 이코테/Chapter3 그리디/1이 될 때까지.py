# N,K 입력
N, K = map(int, input().split())

count = 0 # 수행 횟수
while N != 1:
    if N >= K and N % K == 0:  # N이 K보다 크거나 같고 N이 K로 나누어 떨어지면 N을 K로 나누기
        N /= K
        count += 1
        continue
    else:  # N이 K보다 작거나 N이 K로 나누어 떨어지지 않으면 1 빼기
        N -= 1
        count += 1

print(count) # 결과 값 출력

"""
n, k = map(int, input().split())
result = 0

while True:
    target = (n//k) * k
    result += (n-target)
    n = target
    if n < k:
        break
    result += 1
    n //= k
    
result += (n-1)
print(result)
"""