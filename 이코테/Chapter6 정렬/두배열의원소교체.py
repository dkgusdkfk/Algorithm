# N, K 입력
N, K = map(int, input().split())

# 배열 A, B 입력
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# K번 바꿔치기
for k in range(K):
    A[A.index(min(A))], B[B.index(max(B))] = B[B.index(max(B))], A[A.index(min(A))]

# 배열 A의 모든 원소의 합
result = 0
for n in range(N):
    result += A[n]

# 결과 출력
print(result)