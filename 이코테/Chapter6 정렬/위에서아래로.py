# N입력
N = int(input())

# N개의 수 입력
Nums = []
for n in range(N):
    Nums.append(int(input()))

# 정렬
Nums = sorted(Nums, reverse=True)

# 결과출력
for n in range(N):
    print(Nums[n], end=" ")